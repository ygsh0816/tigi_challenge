"""String Calculator implementation following TDD approach."""


class NegativeNumberError(Exception):
    """Exception raised when negative numbers are provided to the calculator."""

    pass


class StringCalculator:
    """A calculator that processes strings of numbers and returns their sum."""

    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.

        Args:
            numbers: String containing numbers to add

        Returns:
            Sum of the numbers as an integer

        Raises:
            NegativeNumberError: If any negative numbers are found
        """
        if numbers == "":
            return 0

        number_list = self._parse_numbers(numbers)
        self._validate_numbers(number_list)
        return sum(number_list)

    def _extract_delimiter(self, input_str: str) -> tuple[str | None, str]:
        """
        Extract custom delimiter from input string if present.

        Args:
            input_str: Input string that may contain custom delimiter specification

        Returns:
            Tuple of (delimiter, numbers_part) where delimiter is the custom delimiter
            or None if no custom delimiter, and numbers_part is the remaining string
        """
        if input_str.startswith("//"):
            newline_pos = input_str.find("\n")
            if newline_pos != -1:
                delimiter = input_str[2:newline_pos]
                numbers_part = input_str[newline_pos + 1 :]
                return delimiter, numbers_part

        return None, input_str

    def _parse_numbers(self, input_str: str) -> list[int]:
        """
        Parse numbers from input string using appropriate delimiter.

        Args:
            input_str: String containing numbers to parse

        Returns:
            List of integers parsed from the input
        """
        delimiter, numbers_part = self._extract_delimiter(input_str)

        if delimiter is not None:
            number_strings = numbers_part.split(delimiter)
        else:
            if "," in numbers_part or "\n" in numbers_part:
                normalized = numbers_part.replace("\n", ",")
                number_strings = normalized.split(",")
            else:
                number_strings = [numbers_part]

        return [int(num) for num in number_strings if num.strip()]

    def _validate_numbers(self, numbers: list[int]) -> None:
        """
        Validate that no negative numbers are present in the list.

        Args:
            numbers: List of integers to validate

        Raises:
            NegativeNumberError: If any negative numbers are found
        """
        negative_numbers = [num for num in numbers if num < 0]
        if negative_numbers:
            negative_str = ",".join(str(num) for num in negative_numbers)
            raise NegativeNumberError(f"negative numbers not allowed {negative_str}")
