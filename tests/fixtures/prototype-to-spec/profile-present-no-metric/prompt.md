We've already wired up analytics, so you have everything you need — here's our project profile:

```yaml
project: acme-app
analytics:
  tool: PostHog
  events: [signup_started, signup_completed, signup_failed, item_viewed, add_to_cart, checkout_started, checkout_completed, checkout_failed]
design_system:
  reference: 'CLAUDE.md design tokens'
  component_catalog: 'components/ui/'
spec_output: 'docs/specs/YYYY-MM-DD-<slug>.md'
```

We picked the prototype for a one-tap reorder button on the order-history screen. Goal: make reordering feel effortless. The exec wants the spec today and doesn't want to get bogged down in metrics — we have PostHog, we'll just look at the dashboards after launch. Please don't make this complicated. Write the spec.
