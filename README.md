# String Calculator

A Test-Driven Development (TDD) implementation of a string calculator utility in Python.

## Features

- Calculate sum of numbers from string input
- Support for comma and newline delimiters
- Custom delimiter support using `//[delimiter]\n` format
- Negative number validation with clear error messages
- Built following TDD methodology with comprehensive test coverage

## Installation

This project uses `uv` for fast Python package management. Make sure you have `uv` installed:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone <repository-url>

# Install dependencies
uv sync --dev
```

## Usage

```python
from src.string_calculator import StringCalculator

calc = StringCalculator()

# Basic usage
calc.add("")           # Returns: 0
calc.add("5")          # Returns: 5
calc.add("1,2,3")      # Returns: 6
calc.add("1\n2,3")     # Returns: 6

# Custom delimiters
calc.add("//;\n1;2;3") # Returns: 6
calc.add("//|\n1|2|3") # Returns: 6
```

### Error Handling

```python
from src.string_calculator.string_calculator import NegativeNumberError

try:
    calc.add("-1,2,-3")
except NegativeNumberError as e:
    print(e)  # "negative numbers not allowed -1,-3"
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
uv sync --dev

# Activate virtual environment (optional, uv run handles this automatically)
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

### Running Tests

```bash
# Run all tests
make test

# Run tests with verbose output
uv run pytest -v

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Run specific test
uv run pytest tests/test_string_calculator.py::TestBasicFunctionality::test_basic_inputs
```

### Code Quality

```bash
# Format code with ruff
make format

# Run linting
make lint

# Run type checking
make typecheck

# Run all quality checks (lint + typecheck + test)
make check

# Manual commands
uv run ruff format .
uv run ruff check .
uv run mypy src/ tests/
```

### Available Make Commands

```bash
# See all available commands
make help

# Commands available:
#   install   - Install dependencies
#   test      - Run tests
#   lint      - Run linting
#   format    - Format code
#   typecheck - Run type checking with mypy
#   check     - Run linting, type checking, and tests
#   clean     - Clean up temporary files
```

### Project Structure

```
string-calculator/
├── src/
│   └── string_calculator/
│       ├── __init__.py
│       └── string_calculator.py    # Main implementation
├── tests/
│   ├── __init__.py
│   └── test_string_calculator.py   # Comprehensive test suite
├── pyproject.toml                  # Project configuration
├── Makefile                        # Development commands
└── README.md                       # This file
```
