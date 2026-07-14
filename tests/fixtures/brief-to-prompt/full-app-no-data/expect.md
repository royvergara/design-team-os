A full-app builder (Bolt) request. The brief has scope but no definition of what good looks like, and no answer to the full-app data question (what data the prototype needs, whether mocked data is acceptable). Canonical brief-to-prompt stops and lists the missing answers.

MUST: return the list of missing answers, including the data-mocking question the full-app adapter requires, and write NO prompt.
MUST NOT: write a Bolt prompt around the gaps.
MUST NOT: silently assume the quality bar or the data shape.
