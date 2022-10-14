# Noko celebrations

A python project for generating celebrations whenever a user has completed a [Noko](https://nokotime.com) timesheet.

## Running

```sh
NOKO_TOKEN=<noko_api_token> poetry run python run.py
```

This will generate an output similar too:

**Note**: Full completions = 8 hours per day or 40 hours per week and is currently hardcoded

```
Yesterday
  Partial completions
    Sam Bryant: 1.0 hours
  Full completions
    Fred Flintstone: 8.0 hours

This week
  Partial completions
    Sam Bryant: 1.0 hours
  Full completions
    Fred Flintstone: 40.0 hours

Last week
  Partial completions
    Fred Flintstone: 36.0 hours
  Full completions
    Sam Bryant: 40.0 hours
```
