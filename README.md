# String Calculator

A Test-Driven Development (TDD) implementation of a string calculator utility in Python.

## Features

- Calculate sum of numbers from string input
- Support for comma and newline delimiters
- Custom delimiter support using `//[delimiter]\n` format
- Negative number validation with clear error messages
- Built following TDD methodology with comprehensive test coverage

## Installation

```bash
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

### Running Tests

```bash
# Run all tests
make test

# Run with verbose output
uv run pytest -v
```

### Code Quality

```bash
# Format and lint code
make format
make lint

# Run both linting and tests
make check
```
