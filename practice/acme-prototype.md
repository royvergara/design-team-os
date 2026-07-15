# Acme — generated prototype, first candidate (for step 5)

Generated in v0 from the brief's prompt. The designer thinks it's close and wants it on
Thursday's review agenda. Description of what exists (treat as the prototype):

## What the prototype shows

- **Post-signup screen:** a "Set up your workspace" panel with four ordered steps
  (name your workspace → create first board → add a data source → invite your team),
  each with a one-line description and a Start button.
- **Progress:** steps check off as completed; a progress ring shows 0–4. State persists
  on refresh (mocked as local state with a TODO for server-side).
- **Step screens:** each step opens a focused modal with the relevant form; completing it
  returns to the panel with the next step highlighted.
- **Invite step:** step 4 opens the standard invite flow with role selection; sending an
  invite marks the step complete.
- **Visual:** uses the design-system components throughout; desktop layout only so far.

## What is not in this build

- No view for a returning user who left setup half-done (the panel only renders on first
  visit; on return the workspace opens to the default empty board).
- No skip control — guidance can't be dismissed, and there's no way back to it if it could be.
- SSO-created workspaces not handled (flow assumes self-serve signup).
- Error and loading states not designed for the step forms.
