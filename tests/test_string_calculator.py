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

    def test_multiple_comma_separated_numbers_different_values(self):
        """Test that multiple comma-separated numbers work with different values"""
        calculator = StringCalculator()
        result = calculator.add("2,4,6,8,10")
        assert result == 30

    def test_many_comma_separated_numbers(self):
        """Test that many comma-separated numbers work correctly"""
        calculator = StringCalculator()
        result = calculator.add("1,2,3,4,5,6,7,8,9,10")
        assert result == 55

    def test_newline_separated_numbers(self):
        """Test that newline-separated numbers return their sum"""
        calculator = StringCalculator()
        result = calculator.add("1\n2\n3")
        assert result == 6

    def test_multiple_newline_separated_numbers(self):
        """Test that multiple newline-separated numbers work correctly"""
        calculator = StringCalculator()
        result = calculator.add("1\n2\n3\n4\n5")
        assert result == 15

    def test_mixed_comma_and_newline_delimiters(self):
        """Test that mixed comma and newline delimiters work correctly"""
        calculator = StringCalculator()
        result = calculator.add("1\n2,3")
        assert result == 6
