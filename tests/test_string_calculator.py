import pytest
from src.string_calculator import StringCalculator


class TestStringCalculator:
    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0"""
        calculator = StringCalculator()
        result = calculator.add("")
        assert result == 0