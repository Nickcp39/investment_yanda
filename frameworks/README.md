# Investment Frameworks

This folder stores reusable investor "skills": principles, checklists, failure
modes, and review prompts that can be applied across companies, sectors, and
market regimes.

The intent is to keep method separate from evidence:

- `sources/` stores raw inputs and source manifests.
- `companies/`, `sectors/`, `macro/`, and `theses/` store research outputs.
- `frameworks/` stores the judgment models used to interrogate those outputs.

## Suggested Layout

```text
frameworks/
  investor_agents.md
  tech_investor_watchlist.md
  agent_testing/
    README.md
    preference_adjusted_panel.md
    approved_agents.md
    rubric.md
    benchmark_cases.md
    benchmark_cases.jsonl
    scorecard_template.md
    source_grounding_matrix.md
  buffett/
    principles.md
    checklist.md
    quotes_and_sources.md
  munger/
    principles.md
    checklist.md
    mental_models.md
  duan-yongping/
    application_example.md
    principles.md
    checklist.md
    quotes_and_sources.md
  _template.md
```

Start with `investor_agents.md` when you want a quick multi-agent panel before
writing a full thesis. Expand individual folders when one investor lens becomes
important enough to deserve deeper source notes and checklists.

Use `agent_testing/` before trusting any generated or pre-trained investor
agent. A named agent should be treated as unapproved until it passes source
fidelity, boundary, application, adversarial, and cross-agent debate tests.

Each framework should separate:

- Primary source excerpts and links.
- Interpreted principles.
- Practical checklist questions.
- Common misuses or overextensions.
- Examples where the framework would have helped or failed.
