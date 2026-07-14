#!/usr/bin/env python3
"""Regenerate templates/ai-outcomes-scorecard.example.html from templates/scorecard.html.

The committed example is the template's own post-runtime DOM, captured and frozen:
this script fills the template's tokens with the canonical reference data below,
renders it in headless Chrome so the chart runtime draws every figure, dumps the
DOM, then strips the machinery (the :root token blocks, the DATA + chart scripts)
and resolves every var() to its light-register hex — matching the static-example
convention (no tokens, no vars, one reveal script).

Run it whenever templates/scorecard.html changes:

    python3 scripts/regen-example.py            # writes the example in place
    python3 scripts/regen-example.py --check    # exit 1 if the committed example is stale

Requires Chrome/Chromium on the machine (CHROME env var overrides discovery).
The reference data below is the design source of truth for the example's content;
edit it here, never by hand-editing the generated file.
"""

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "scorecard.html"
EXAMPLE = ROOT / "templates" / "ai-outcomes-scorecard.example.html"

# ---------------------------------------------------------------- reference data

GLANCE = [
    {"G_LABEL": "Day-7 activation", "G_VALUE_CLASS": "miss",
     "G_VALUE": '47<span style="font-size:0.42em;vertical-align:0.85em;">%</span>',
     "G_FROM": "from 34% · goal 50%", "G_DELTA_CLASS": "miss", "G_DELTA": "Below bar"},
    {"G_LABEL": "Time to validated learning", "G_VALUE_CLASS": "met", "G_VALUE": "3 days",
     "G_FROM": "from 3 weeks", "G_DELTA_CLASS": "met", "G_DELTA": "7× faster"},
    {"G_LABEL": "Cost per validated learning", "G_VALUE_CLASS": "met", "G_VALUE": "$1.1k",
     "G_FROM": "from $8k", "G_DELTA_CLASS": "met", "G_DELTA": "86% cheaper"},
]

KILLS = [
    {"K_DIRECTION": "Checklist-first onboarding", "K_DIED_AT": "Triage · final",
     "K_COST": "$0.7k", "K_WHY": "2/6 brief criteria; completion theater, no invite path"},
    {"K_DIRECTION": "Video walkthrough overlay", "K_DIED_AT": "Critique · cut",
     "K_COST": "$1.5k", "K_WHY": "Attitudinal read: 3/10 finished it; scoped at ~6 build-weeks"},
]

BEATS = [
    {"B_STATE": "met", "B_WHEN": "2026-05-12 · Prototype — Attitudinal",
     "B_TEXT": '9/10 completed setup unaided; SUS 81. <strong style="color:var(--accent);">Met.</strong>',
     "B_WAFFLE_FILLED": "9", "B_WAFFLE_TOTAL": "10"},
    {"B_STATE": "met", "B_WHEN": "2026-05-26 · Prototype — Behavioral",
     "B_TEXT": '7/10 sent a teammate invite inside the prototype task. <strong style="color:var(--accent);">Met.</strong>',
     "B_WAFFLE_FILLED": "7", "B_WAFFLE_TOTAL": "10"},
    {"B_STATE": "miss", "B_WHEN": "2026-07-01 · Six weeks post-ship — Performance",
     "B_TEXT": 'Day-7 activation 34% → 47% against the 50% bar. <strong style="color:var(--miss);">Below bar</strong>, still climbing.',
     "B_WAFFLE_FILLED": "0", "B_WAFFLE_TOTAL": "0"},
    {"B_STATE": "next", "B_WHEN": "2026-09-30 · Q3 close",
     "B_TEXT": "Final read. The verdict on this page is provisional until then.",
     "B_WAFFLE_FILLED": "0", "B_WAFFLE_TOTAL": "0"},
]

BETS = [
    {"BET_OVERDUE_CLASS": "", "BET_WORK": "“Invite a teammate” nudge on the empty state",
     "BET_OWNER": "Priya N.", "BET_REVIEW_BY": "2026-06-30",
     "BET_FINDING": '<span class="chip chip-teal" style="margin-bottom:7px;">Bet paid</span><br>'
                    'Nudge-attributed invites = <span class="num" style="color:var(--ink);font-weight:600;">22%</span>'
                    ' of day-7 activations. Folding into the default flow.'},
]

DATA = {
    "outcome": {"baseline": 34, "current": 47, "bar": 50, "state": "miss",
                "baselineLabel": "Apr · baseline", "currentLabel": "Jul · 6 wks post-ship",
                "finalLabel": "Sep · Q3 close",
                "unreadNote": ["6 of 13 weeks still maturing", "Final read · Sep 30"],
                "gridTicks": [35, 45, 55]},
    "confidence": 70,
    "leverage": [
        {"label": "Brief to validated prototype", "serves": "attitudinal",
         "was": 21, "now": 3, "target": 2, "wasLabel": "3 wk", "nowLabel": "3 days", "targetLabel": "target 2 days"},
        {"label": "Directions explored per brief", "serves": "behavioral",
         "was": 1.5, "now": 5, "target": 4, "wasLabel": "1.5", "nowLabel": "5", "targetLabel": "target 4"},
        {"label": "Cost per validated learning", "serves": "attitudinal",
         "was": 8000, "now": 1100, "target": 1000, "wasLabel": "$8k", "nowLabel": "$1.1k", "targetLabel": "target $1k"},
        {"label": "Decisions backed by a real user signal", "serves": "all three",
         "was": 20, "now": 75, "target": 80, "wasLabel": "20%", "nowLabel": "75%", "targetLabel": "target 80%"},
    ],
    "price": {"avoided": 85000, "spent": 2200, "avoidedLabel": "~$85k", "spentLabel": "$2.2k"},
}

SCALARS = {
    "EFFORT_NAME": "Self-serve onboarding redesign",
    "OWNER": "Priya N., Head of Design",
    "GENERATED_DATE": "2026-07-14",
    "CLASS_CHIP": "Exploration bet",
    "FOLIO_CLASSIFICATION": "Confidential",
    "FOLIO_PERIOD": "Q3 FY26",
    "HEADLINE_MAIN": 'Learning got 7<span style="font-size:0.62em;">&times;</span> faster. Activation rose 13 points',
    "HEADLINE_MISS_PHRASE": "— 3 short of the bar.",
    "HERO_VALUE": "47",
    "HERO_LABEL": "Day-7 activation",
    "HERO_CAPTION_1": "+13 pts from 34%",
    "HERO_CAPTION_2": "below a 50% bar",
    "DECK": 'Time to validated learning compressed from <strong style="color:var(--ink);font-weight:600;">3 weeks to 3 days</strong>; '
            'day-7 activation moved <strong style="color:var(--ink);font-weight:600;">34% &rarr; 47%</strong> against a '
            'pre-registered bar of <strong style="color:var(--ink);font-weight:600;">50%</strong> — still climbing, '
            'reads final at Q3 close (2026-09-30).',
    "BAR_STAMP": "Locked 2026-04-02 · pre-build",
    "PAIN": 'New admin, verbatim: <em style="color:var(--ink);font-style:italic;">“I signed up and had no idea what to do next.”</em>',
    "GOAL": "Day-7 activation — workspace created + one teammate invited.",
    "BAR_LINE": "34% &rarr; 50%",
    "LEAD_1": "The commitment, made in the open before any build — a named pain, one metric, and the bar we agreed would count as solving it.",
    "LEAD_2": "Where speed paid off and where discipline drew the line — the leverage AI bought, and the directions killed early for a fraction of their build cost.",
    "LEAD_3": "Every measured read in the order it landed — the prototype signals that cleared, then the shipped outcome against the pre-registered bar.",
    "VERDICT_1": "We called the onboarding leak at 70% confidence, and set the bar before a single prototype existed.",
    "VERDICT_2": "Two directions were wrong for $2.2k — not for the $85k they were scoped to cost.",
    "VERDICT_3": "The speed is proven. The outcome is measured, honest, and three points short — it reads final in September.",
    "VERDICT_5": "This scorecard closes on September 30, when the number — not the narrative — decides.",
    "PROSE_NEXT_READ": "Activation holds a 13-point gain with 6 of 13 weeks of cohort data still to mature. The bar stays 50%; "
                       "nothing on this page moves it. If the final read clears, the pattern folds into the default flow; if it "
                       "misses, the readout hands strategy the next problem — the invite step, where the funnel now thins.",
    "SOURCE_FILENAME": "ai-outcomes-scorecard.md",
}

# var() -> light-register hex, derived tokens first so e.g. --accent-2 wins over --accent
VAR_TO_HEX = [
    ("var(--accent-2)", "#1b8a7c"), ("var(--accent-rgb)", "21,125,111"), ("var(--accent)", "#157d6f"),
    ("var(--ink-rgb)", "19,50,45"), ("var(--ink)", "#13322d"),
    ("var(--miss-rgb)", "161,85,63"), ("var(--miss)", "#a1553f"),
    ("var(--amber-rgb)", "146,112,22"), ("var(--amber)", "#927016"),
    ("var(--muted-2)", "#8e988f"), ("var(--muted)", "#606f69"), ("var(--faint)", "#b9c0b7"),
    ("var(--track-2)", "#d6dcd1"), ("var(--track-3)", "#ccd2c8"), ("var(--track)", "#e5e8df"),
    ("var(--grid)", "#eff1e9"), ("var(--paper)", "#f3f5f1"), ("var(--panel)", "#fcfdfb"),
    ("var(--badge-bg)", "#042f2e"), ("var(--badge-fg)", "#40e0d0"),
]

# ---------------------------------------------------------------- pipeline


def expand(tpl, name, rows):
    m = re.search(r"<!-- repeat:" + name + r" -->(.*?)<!-- /repeat:" + name + r" -->", tpl, re.S)
    if not m:
        sys.exit(f"repeat block not found in template: {name}")
    block, out = m.group(1), ""
    for row in rows:
        b = block
        for k, v in row.items():
            b = b.replace("{{" + k + "}}", v)
        out += b
    return tpl[: m.start()] + out + tpl[m.end():]


def fill_template():
    tpl = TEMPLATE.read_text()
    tpl = expand(tpl, "glance", GLANCE)
    tpl = expand(tpl, "kill", KILLS)
    tpl = expand(tpl, "beat", BEATS)
    tpl = expand(tpl, "bet", BETS)
    tpl = tpl.replace("<!-- state:bets -->", "").replace("<!-- /state:bets -->", "")
    for k, v in SCALARS.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    tpl = tpl.replace("{{DATA_JSON}}", json.dumps(DATA))
    left = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", tpl)))
    if left:
        sys.exit(f"unfilled tokens after fill: {left} — update SCALARS/repeat data in this script")
    return tpl


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "google-chrome", "google-chrome-stable", "chromium-browser", "chromium",
    ]
    for c in candidates:
        if c.startswith("/") and pathlib.Path(c).exists():
            return c
        if shutil.which(c):
            return c
    sys.exit("Chrome/Chromium not found — set CHROME=/path/to/chrome")


def dump_dom(filled_html):
    chrome = find_chrome()
    with tempfile.TemporaryDirectory() as td:
        page = pathlib.Path(td, "filled.html")
        page.write_text(filled_html)
        out = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--virtual-time-budget=6000",
             "--dump-dom", f"file://{page}"],
            capture_output=True, text=True, timeout=120,
        )
        if not out.stdout or "<body" not in out.stdout:
            sys.exit(f"chrome --dump-dom produced no document (stderr: {out.stderr[:200]})")
        return out.stdout


def to_example(dom):
    head = dom[dom.index("<head>") + 6: dom.index("</head>")]
    body = dom[dom.index("<body>") + 6: dom.index("</body>")]
    title = re.search(r"<title>.*?</title>", head, re.S).group(0)
    style = re.search(r"<style>.*?</style>", head, re.S).group(0)
    # strip the token machinery: light root, dark root, dark print override
    style = re.sub(r"\s*:root\{[^}]*\}", "", style)
    style = re.sub(r'\s*:root\[data-theme="dark"\]\{[^}]*\}', "", style)
    style = re.sub(r'\s*@media print\{\s*:root\[data-theme="dark"\]\{[^}]*\}\s*\}', "", style)
    # drop the DATA + chart-runtime scripts; keep only the reveal/progress script
    for s in re.findall(r"<script>.*?</script>", body, re.S):
        if "IntersectionObserver" not in s:
            body = body.replace(s, "")
    body = body.replace('<div id="progress" style="width: 0%;"></div>', '<div id="progress"></div>')
    body = body.replace('class="reveal in"', 'class="reveal"')
    frag = title + "\n" + style + "\n" + body.strip() + "\n"
    for a, b in VAR_TO_HEX:
        frag = frag.replace(a, b)
    leftovers = sorted(set(re.findall(r"var\(--[a-z0-9-]+\)", frag)))
    if leftovers:
        sys.exit(f"unresolved var() after hex pass: {leftovers} — extend VAR_TO_HEX")
    if "{{" in frag:
        sys.exit("template tokens leaked into the example")
    return frag


def main():
    check = "--check" in sys.argv
    frag = to_example(dump_dom(fill_template()))
    if check:
        if EXAMPLE.read_text() == frag:
            print("regen check: OK — committed example matches the template")
            return 0
        print("regen check: STALE — templates/scorecard.html changed; run scripts/regen-example.py")
        return 1
    EXAMPLE.write_text(frag)
    print(f"wrote {EXAMPLE.relative_to(ROOT)} ({len(frag)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
