# Search treats user input as SQL

## Type
Bug / security

## Current behavior
`search_products` inserts the search term directly into a SQL string. A crafted term can change the meaning of the query and return products that do not match the intended search.

## Expected behavior
The search term must always be treated as data. A term containing SQL control characters should return only literal matches and must not alter the query.

## Reproduction value
Use this synthetic term in a test:

```text
' OR 1=1 --
```

With the demo data, the expected result is an empty list.

## Acceptance criteria
- A test fails before the fix and passes after the fix.
- The query uses bound parameters.
- Existing search behavior remains unchanged.
- `pytest -q`, `ruff check .`, and `bandit -r app -q` pass.
- The changelog is updated.
