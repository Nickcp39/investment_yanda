# Model — GEV

This folder holds the valuation scenario structure behind `../valuation.md`.

Keep model files boring and auditable:
- Explicit units; source IDs in notes.
- Separate historical actuals from forecasts.
- Bear/base/bull assumptions visible.

⚠️ **GEV-specific:** an owner-earnings DCF is **not** the right primary tool — the trailing base is one-off-distorted (tax release + M&A gains + advance-payment FCF) and the equipment-pricing premium is cyclical. So the model triangulates on **normalized EBITDA × EV/EBITDA → price**.

Files:
```text
model_assumptions.md     # drivers, anchor actuals, bear/base/bull logic
scenario_model.csv       # normalized EBITDA x multiple -> implied price
```
