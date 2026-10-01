# Test Strategy

This document explains what the framework tests, why, and how the testing is prioritized. It applies to the two practice systems used in this repository:

- **UI:** [saucedemo.com](https://www.saucedemo.com), an e-commerce demo site (login, product list, cart, checkout)
- **API:** [dummyjson.com](https://dummyjson.com), a public REST API (products resource)

## 1. Objectives

1. Protect the most important user journeys with fast, reliable automated checks.
2. Give quick feedback on every code change through CI.
3. Keep the suite maintainable: when the UI changes, the fix happens in one place.

## 2. Scope

**In scope**

| Area | Coverage |
|------|----------|
| Login | Valid login; locked-out user, wrong password, empty username, empty password |
| Product list | Sorting by price; adding and removing items |
| Cart | Badge count, items shown in cart |
| Checkout | Complete purchase; mandatory-field validation |
| API (products) | GET list, GET single (schema check), POST, PUT, DELETE, 404 for unknown id |

**Out of scope (and why)**

- Performance and load testing: the target sites are shared public services and are not suitable for load.
- Security testing: same reason; testing public sites beyond normal use is not appropriate.
- Cross-browser and mobile: the suite runs on Chromium only for now. Adding Firefox and WebKit is a configuration change.
- Visual and accessibility testing: not covered yet.

## 3. Risk-based prioritization

Tests are prioritized by business impact and likelihood of failure.

| Priority | Flow | Reason | Marker |
|----------|------|--------|--------|
| High | Login, add to cart, complete checkout | Revenue-critical; a failure blocks every user | `smoke` |
| High | API availability and basic CRUD | Every client depends on it | `smoke` |
| Medium | Invalid login messages, checkout validation | Affects user experience and support load | `regression` |
| Medium | Cart updates, price sorting | Common actions, lower impact when broken | `regression` |
| Low | Unknown-id handling | Edge case | `regression` |

## 4. Test levels and approach

- **UI tests (Playwright + Pytest):** end-to-end user flows through the browser, using the Page Object Model.
- **BDD scenarios (pytest-bdd):** the key journeys are also written in Gherkin so that business and QA can read and review the expected behaviour. They reuse the same Page Objects and API client.
- **API tests (requests + Pytest):** status codes, response schema and response content, run without a browser so they are fast.
- **Data-driven tests:** negative login cases are stored in `data/users.json` and run as parameterized tests.
- **Test design techniques:** equivalence partitioning (valid and invalid credentials), boundary and empty-input checks, and negative testing.

## 5. Execution strategy

| When | What runs | Command |
|------|-----------|---------|
| During development | Smoke tests | `pytest -m smoke` |
| Every push and pull request | Full suite in GitHub Actions | `pytest` |
| On demand | BDD scenarios only | `pytest -m bdd` |
| On demand | API only or UI only | `pytest -m api` or `pytest -m ui` |

## 6. Entry and exit criteria

**Entry:** dependencies installed, target site reachable, test data available in `data/`.

**Exit (a run is acceptable when):**
- All smoke tests pass.
- Regression pass rate is 100%, or every failure is triaged and logged as a defect or a known issue.
- The HTML report is generated and uploaded as a CI artifact.

## 7. Defect handling and flaky tests

- Failed UI tests save a screenshot in `reports/artifacts/`.
- A failure is first checked for test problems (locator, timing, data) before being reported as a product defect.
- Playwright's auto-waiting and web-first assertions are used instead of fixed sleeps, to reduce flaky tests.
- A test that fails intermittently is investigated and fixed, not simply re-run.

## 8. Metrics

| Metric | How it is measured |
|--------|--------------------|
| Pass rate | HTML report per run |
| Execution time | CI run duration |
| Coverage of critical flows | Smoke markers versus the priority table above |
| Flakiness | Tests that fail and then pass without a code change |

## 9. Known limitations and next steps

- The target sites are third-party practice sites, so a site outage can fail the suite without a real defect.
- Possible next steps: add Firefox and WebKit runs, parallel execution (`pytest-xdist`), an Allure report, and a basic accessibility check.
