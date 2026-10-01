# QA Automation Framework

![CI](https://github.com/sayedadelqa/qa-automation-framework/actions/workflows/ci.yml/badge.svg)

UI and API test automation framework built with **Playwright, Python and Pytest**, using the Page Object Model, **BDD scenarios in Gherkin (pytest-bdd, the Python equivalent of Cucumber)**, and a GitHub Actions CI pipeline.

## What it tests
- **UI** ([saucedemo.com](https://www.saucedemo.com), a public practice site): login (valid and invalid), cart, sorting, checkout.
- **API** ([dummyjson.com](https://dummyjson.com), a public practice API (products)): GET, POST, PUT, DELETE, status codes and response schema.

## Project structure
```
pages/        Page Objects (one class per page)
tests/ui/     UI tests
tests/api/    API tests
tests/bdd/    BDD tests: features/ (Gherkin .feature files) and step definitions
api/          API client wrapper around requests
data/         Test data in JSON (no data inside test code)
utils/        Config and helpers
conftest.py   Shared fixtures
pytest.ini    Pytest settings and markers
reports/      HTML report and failure screenshots (generated)
.github/workflows/ci.yml   CI pipeline
```

## Run locally
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
playwright install chromium
pytest
```

Useful commands:
```bash
pytest -m smoke          # critical flows only
pytest -m api            # API tests only
pytest -m ui --headed    # watch the browser
pytest -m bdd            # BDD scenarios only
```

Report: `reports/report.html`. Screenshots of failures: `reports/artifacts/`.

## BDD (Gherkin)
Business-readable scenarios live in `tests/bdd/features/*.feature` and are written in Given/When/Then style. Step definitions in `tests/bdd/` reuse the same Page Objects and API client as the plain Pytest tests, so there is no duplicated page logic.

```gherkin
Scenario: Adding an item updates the cart badge
  When the user adds "Sauce Labs Backpack" to the cart
  Then the cart badge shows 1
```
Tags such as `@smoke`, `@regression`, `@ui` and `@api` become Pytest markers, so `pytest -m "bdd and smoke"` works.

## Design decisions
- **Page Object Model**: locators and page actions live in `pages/`, so UI changes are fixed in one place.
- **Data-driven**: test data in `data/users.json`, and invalid logins run as parameterized tests.
- **Markers**: `smoke` and `regression` let CI or developers run only what they need.
- **BDD on top of the same layers**: feature files describe behaviour, steps only call Page Objects, and Page Objects own the locators.
- **CI**: every push runs the full suite on GitHub Actions and uploads the report.

See [TEST_STRATEGY.md](TEST_STRATEGY.md) for scope, risks and priorities.
