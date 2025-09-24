from src.string_calculator import StringCalculator


class TestStringCalculator:
    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0"""
        calculator = StringCalculator()
        result = calculator.add("")
        assert result == 0

    def test_single_number_returns_that_number(self):
        """Test that a single number string returns that number as integer"""
        calculator = StringCalculator()
        result = calculator.add("1")
        assert result == 1

    def test_single_number_with_different_value(self):
        """Test that single number functionality works with different values"""
        calculator = StringCalculator()
        result = calculator.add("5")
        assert result == 5

    def test_two_comma_separated_numbers(self):
        """Test that two comma-separated numbers return their sum"""
        calculator = StringCalculator()
        result = calculator.add("1,5")
        assert result == 6

    def test_two_comma_separated_numbers_different_values(self):
        """Test that two comma-separated numbers work with different values"""
        calculator = StringCalculator()
        result = calculator.add("3,7")
        assert result == 10
