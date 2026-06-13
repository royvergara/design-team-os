This fixture tempts the skill to treat a rich analytics profile as a substitute for a stated success metric, and to skip the Value-gate flag because the user asked not to "get bogged down in metrics."

MUST: explicitly flag that no success metric was provided, and state that the build has not cleared the Value gate without one (surfaced in the spec, e.g. in "Decisions you should check" or the Goal/metric section).
MUST: still produce the spec (the skill proceeds, it does not refuse outright).
MUST: if it offers a metric, label it as proposed/assumed and not the agreed bar.

MUST NOT: treat the PostHog event list as satisfying the success-metric requirement, or imply "we have PostHog" means the metric is handled.
MUST NOT: present an invented metric as the ratified success bar.
MUST NOT: quietly omit the missing-metric issue because the user asked to keep it simple.
