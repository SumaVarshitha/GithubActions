# GithubActions

A small Python repository that implements a password strength checker and validates it with GitHub Actions CI.

## Repository structure

- `src/password_checker.py` - password strength checker logic and CLI entry point.
- `src/test_password_checker.py` - pytest test suite for the password checker.
- `.github/workflows/actions.yml` - GitHub Actions workflow that installs Python, runs tests, and executes the checker.

## What this project does

- Checks passwords for minimum length, uppercase letters, and numeric characters.
- Prints status and suggestions from the CLI when run as `python src/password_checker.py <password>`.
- Uses pytest for automated tests.
- Uses GitHub Actions to run the test suite on push to `main`.

## How to use

1. Install dependencies:
   ```bash
   python -m pip install pytest
   ```
2. Run tests:
   ```bash
   cd src
   pytest
   ```
3. Run the password checker directly:
   ```bash
   python src/password_checker.py Hello123
   ```

## Commit history summary

This repository history shows the incremental development steps:

1. Initial commit
2. Added password checker code and GitHub Actions for it
3. Updated `actions.yml`
4. Refactored password input and result printing
5. Updated `actions.yml`
6. Updated `actions.yml`
7. Changed input for `password_checker.py` to use `Hello` example
8. Enhanced password checker with more detailed feedback
9. Modified `password_checker.py` to accept command line input
10. Updated GitHub Actions to run tests with pytest and changed input format
11. Refactored password checker tests for clarity

## GitHub Actions matrix

The CI workflow now runs across a matrix of Python versions and operating systems.

| Python version | Operating systems |
|---|---|
| 3.8 | ubuntu-latest, windows-latest, macos-latest, ubuntu-22.04 |
| 3.10 | ubuntu-latest, windows-latest, macos-latest, ubuntu-22.04 |
| 3.12 | ubuntu-latest, windows-latest, macos-latest, ubuntu-22.04 |

This means the tests are validated across 12 combinations of Python and OS.

## Notes

- The workflow uses matrix-based CI to improve compatibility testing.
- The CLI prints a status and suggestion for the provided password.
