# Student Score Tracker

A small modular Python application used for the **SEN 401 – Software Configuration Management and Maintenance** lab at Miva Open University. It stores a list of students with their scores and prints basic statistics.

## Project Structure

```
sen401-scm-project/
├── app.py              # Entry point – runs the demo application
├── students.py         # Data module – student list and data functions
├── utils/
│   ├── __init__.py     # Makes utils a Python package
│   └── helpers.py      # Utility functions (highest, lowest, pass count)
├── tests/
│   └── test_students.py # Unit tests (unittest)
├── requirements.txt    # Python dependencies
├── .gitignore          # Files Git should not track
└── README.md           # Project documentation
```

## Modules

| File | Description |
|------|-------------|
| `app.py` | Main script. Prints a formatted student table, adds a student and prints a summary report. |
| `students.py` | Holds the `students` list (each student has a `name` and `score`), input validation (`validate_student()`) and statistics: `average_score()`, `median_score()`, `pass_rate()`, plus `add_student()` and `get_students()`. |
| `utils/helpers.py` | Utility functions: `highest_score()`, `lowest_score()` and `pass_count()`. |
| `requirements.txt` | Lists external dependencies (standard library only). |
| `tests/test_students.py` | 14 unit tests covering empty lists, statistics and validation. |

## Requirements

- Python 3.12 or later

## How to Run

```bash
git clone <repository-url>
cd sen401-scm-project
pip install -r requirements.txt
python app.py

# run the tests
python -m unittest discover -s tests -v
```

## Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, released code. Protected – changes only through reviewed pull requests. |
| `dev` | Integration branch for ongoing development. |
| `feature/*` | New features, e.g. `feature/median-score`. |
| `maint/*` | Maintenance work, e.g. `maint/empty-list-fix`. |
| `maintenance` | Lab 2 branch holding all v1.1 maintenance changes. |

## Releases

| Version | Description |
|---------|-------------|
| v1.0 | Initial baseline – core student data, helpers and demo app. |
| v1.1 | Maintenance release – see below. |

### v1.1 maintenance changes

| Type | Change |
|------|--------|
| Corrective | `average_score()`, `highest_score()` and `lowest_score()` no longer crash on an empty list. |
| Adaptive | Updated for Python 3.12+ (type hints, PEP 695 `type` alias); new `validate_student()` input validation using the standard library. |
| Perfective | Added median score and pass rate; aligned table output with PASS/FAIL. |
| Preventive | Refactored `students.py` into sections with constants, docstrings and comments; added unit tests. |
