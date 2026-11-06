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
├── requirements.txt    # Python dependencies
├── .gitignore          # Files Git should not track
└── README.md           # Project documentation
```

## Modules

| File | Description |
|------|-------------|
| `app.py` | Main script. Imports the data and helper modules, adds a student and prints a summary report. |
| `students.py` | Holds the `students` list (each student has a `name` and `score`) and functions `average_score()`, `add_student()` and `get_students()`. |
| `utils/helpers.py` | Utility functions: `highest_score()`, `lowest_score()` and `pass_count()`. |
| `requirements.txt` | Lists external dependencies (none for v1.0). |

## Requirements

- Python 3.12 or later

## How to Run

```bash
git clone <repository-url>
cd sen401-scm-project
pip install -r requirements.txt
python app.py
```

## Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, released code. Protected – changes only through reviewed pull requests. |
| `dev` | Integration branch for ongoing development. |
| `feature/*` | New features, e.g. `feature/median-score`. |
| `maint/*` | Maintenance work, e.g. `maint/empty-list-fix`. |

## Releases

| Version | Description |
|---------|-------------|
| v1.0 | Initial baseline – core student data, helpers and demo app. |
