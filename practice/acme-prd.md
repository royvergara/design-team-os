# Acme PRD — Activation Improvements (v0.3, PM: J. Osei) (for step 2)

## Business goal

Lift day-7 activation (workspace created + ≥1 teammate invited within 7 days) from 34% to
50% this half. Activation is the strongest predictor of month-3 retention in our cohort
data; the 34% floor is the single biggest drag on net revenue retention.

## Customer problem

New workspace admins tell us they don't know what to do after signup: "I signed up and had
no idea what to do next." The funnel confirms it — 38% survive the second setup step, and
27 of 43 recent onboarding tickets are some form of "what do I set up first."

## Proposed direction

A guided setup experience for new workspaces. Candidate shapes discussed internally:
a step-by-step checklist, template galleries, an interactive tour. Design to explore.

## Requirements

1. New admins see a clear "what's next" from the first post-signup screen.
2. Progress through setup is visible and resumable across sessions.
3. Inviting a teammate is reachable from within the setup experience.
4. Users can skip guidance at any time without losing access to it.
5. Works for workspaces created from SSO enterprise invites as well as self-serve.

## Also in this document (from stakeholder review)

- Billing: the annual-plan discount banner should move above the fold on the plans page
  (Finance ask; revenue team owns copy).
- GTM: launch webinar + lifecycle email sequence for the new onboarding (Marketing owns;
  needs a date by end of month).
- Legal: SOC 2 badge must appear in the workspace-creation flow footer.
- Eng platform note: setup state must be stored server-side (mobile app will read it in Q4).

## Timeline

Design exploration now; build slot opens in 6 weeks.
