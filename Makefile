.PHONY: help install test lint format typecheck check clean

help:
	@echo "Available commands:"
	@echo "  install   - Install dependencies"
	@echo "  test      - Run tests"
	@echo "  lint      - Run linting"
	@echo "  format    - Format code"
	@echo "  typecheck - Run type checking with mypy"
	@echo "  check     - Run linting, type checking, and tests"
	@echo "  clean     - Clean up temporary files"

install:
	uv sync --dev

test:
	uv run pytest -v || test $$? -eq 5

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	PYTHONPATH=src uv run mypy src/string_calculator tests/

check: lint typecheck test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +