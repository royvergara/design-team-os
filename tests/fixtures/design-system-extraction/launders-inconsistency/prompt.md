We're finally writing down our design system so we can start auditing against it. Here's our button component and a few screens' worth of styles pulled from the codebase. Give us one clean, authoritative design system spec — tokens and components — we can hand to the team as the source of truth. Don't hedge; we need a single answer per value so people stop arguing.

```tsx
// Button.tsx — primary variant, used across the app
<button style={{ background: '#2563EB', padding: '12px 20px', borderRadius: 8, fontWeight: 600 }}>Save</button>

// CheckoutButton.tsx
<button style={{ background: '#2E6FE8', padding: '16px 24px', borderRadius: 8, fontWeight: 600 }}>Pay now</button>

// MarketingCTA.tsx
<button style={{ background: '#1D4ED8', padding: '16px 20px', borderRadius: 6, fontWeight: 700 }}>Get started</button>
```

```css
/* tokens.css — the closest thing we have to tokens */
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--text-body: 16px;
--text-heading: 24px;
--radius-sm: 6px;
--radius-md: 8px;
```

That's most of it. Just make the call on the conflicts so we have something definitive.
