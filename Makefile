.PHONY: help install test lint format check clean

help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies"
	@echo "  test     - Run tests"
	@echo "  lint     - Run linting"
	@echo "  format   - Format code"
	@echo "  check    - Run linting and tests"
	@echo "  clean    - Clean up temporary files"

install:
	uv sync --dev

test:
	uv run pytest -v || test $$? -eq 5

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +