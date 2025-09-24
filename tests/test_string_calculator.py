import pytest

from src.string_calculator import StringCalculator
from src.string_calculator import NegativeNumberError


@pytest.fixture
def calculator():
    """Fixture to provide a StringCalculator instance for tests."""
    return StringCalculator()


class TestBasicFunctionality:
    """Test basic calculator functionality with simple inputs."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("", 0),
            ("1", 1),
            ("5", 5),
        ],
    )
    def test_basic_inputs(self, calculator, input_str, expected):
        """Test basic inputs: empty string, single numbers."""
        assert calculator.add(input_str) == expected

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("1,5", 6),
            ("3,7", 10),
            ("2,4,6,8,10", 30),
            ("1,2,3,4,5,6,7,8,9,10", 55),
        ],
    )
    def test_comma_separated_numbers(self, calculator, input_str, expected):
        """Test comma-separated numbers with various quantities."""
        assert calculator.add(input_str) == expected


class TestDelimiters:
    """Test different delimiter support."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("1\n2\n3", 6),
            ("1\n2\n3\n4\n5", 15),
        ],
    )
    def test_newline_delimiters(self, calculator, input_str, expected):
        """Test newline-separated numbers."""
        assert calculator.add(input_str) == expected

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("1\n2,3", 6),
            ("10,20\n30,40\n50", 150),
        ],
    )
    def test_mixed_delimiters(self, calculator, input_str, expected):
        """Test mixed comma and newline delimiters."""
        assert calculator.add(input_str) == expected

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("//;\n1;2", 3),
            ("//|\n1|2|3", 6),
            ("//#\n5#10#15", 30),
            ("//;\n1;2;3", 6),
            ("//|\n1|2|3|4|5", 15),
        ],
    )
    def test_custom_delimiters(self, calculator, input_str, expected):
        """Test custom delimiter functionality."""
        assert calculator.add(input_str) == expected


class TestNegativeNumbers:
    """Test negative number validation."""

    def test_single_negative_number(self, calculator):
        """Test that a single negative number throws exception with correct message."""
        expected_message = "negative numbers not allowed -1"
        with pytest.raises(NegativeNumberError, match=expected_message):
            calculator.add("-1")

    def test_multiple_negative_numbers_comma_separated(self, calculator):
        """Test multiple negative numbers with comma delimiter."""
        expected_message = "negative numbers not allowed -1,-3"
        with pytest.raises(NegativeNumberError, match=expected_message):
            calculator.add("-1,2,-3")

    def test_multiple_negative_numbers_custom_delimiter(self, calculator):
        """Test multiple negative numbers with custom delimiter."""
        expected_message = "negative numbers not allowed -1,-3,-4"
        with pytest.raises(NegativeNumberError, match=expected_message):
            calculator.add("//;\n-1;2;-3;-4")

    def test_multiple_negative_numbers_newline_delimiter(self, calculator):
        """Test multiple negative numbers with newline delimiter."""
        expected_message = "negative numbers not allowed -1,-2"
        with pytest.raises(NegativeNumberError, match=expected_message):
            calculator.add("-1\n-2\n3")
