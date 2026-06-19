# Model

This folder holds structured tables and valuation scenarios.

Keep model files boring and auditable:

- Use explicit units.
- Keep source IDs in notes.
- Separate historical facts from forecasts.
- Keep bear/base/bull assumptions visible.

Suggested files:

```text
historicals.csv
segments.csv
owner_earnings_bridge.csv
valuation_scenarios.csv
sensitivity.csv
```

For VRT the scenario engine is **driver → EPS × P/E → price** (`scenario_model.csv`), not an owner-earnings DCF — VRT is FCF-positive and the swing variable is the forward multiple on a high-beta capex-cycle name. Bear/base/bull drivers and the implied price ladder live in `scenario_model.csv`; the reasoning behind each driver is in `model_assumptions.md`.
