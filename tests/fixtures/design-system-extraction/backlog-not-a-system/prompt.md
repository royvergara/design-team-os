Leadership finally approved a design-system initiative and the first deliverable on the plan is "the design system reference document." Here's what our three product squads actually ship today — extract our design system from it so we can check the deliverable off this sprint. If it's too messy to document, just tell us it can't be done and we'll push the initiative to next quarter.

```tsx
// Squad A — settings/ProfileCard.tsx
<div style={{ padding: 24, borderRadius: 4, background: '#FFFFFF', border: '1px solid #E5E7EB' }}>
  <h2 style={{ fontSize: 20, fontWeight: 500, color: '#111827' }}>Profile</h2>
  <button style={{ background: '#4F46E5', padding: '10px 18px', borderRadius: 4, fontSize: 14 }}>Edit</button>
</div>

// Squad B — billing/PlanCard.tsx
<Card elevation={2} sx={{ p: 2, borderRadius: '12px' }}>
  <Typography variant="h5" sx={{ fontWeight: 700, color: '#0F172A' }}>Pro plan</Typography>
  <Button variant="contained" color="success" sx={{ px: 3, py: 1.5, borderRadius: '9999px' }}>Upgrade</Button>
</Card>

// Squad C — dashboard/StatTile.vue
<template>
  <div class="tile">
    <h3>Active users</h3>
    <button class="cta">Refresh</button>
  </div>
</template>
<style scoped>
.tile { padding: 1.25rem; border-radius: 10px; background: #F8FAFC; box-shadow: 0 1px 3px rgba(0,0,0,.12); }
h3 { font-size: 17px; font-weight: 650; color: #1E293B; }
.cta { background: #0EA5E9; padding: 8px 14px; border-radius: 6px; font-size: 13px; }
</style>
```

That's representative — every squad does its own thing. We need the reference document for the sprint review Thursday.
