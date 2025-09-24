"""String Calculator implementation following TDD approach."""


class StringCalculator:
    """A calculator that processes strings of numbers and returns their sum."""

    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.

        Args:
            numbers: String containing numbers to add

        Returns:
            Sum of the numbers as an integer
        """
        if numbers == "":
            return 0

        # Parse numbers using appropriate delimiter
        number_list = self._parse_numbers(numbers)
        return sum(number_list)

    def _extract_delimiter(self, input_str: str) -> tuple[str, str]:
        """
        Extract custom delimiter from input string if present.

        Args:
            input_str: Input string that may contain custom delimiter specification

        Returns:
            Tuple of (delimiter, numbers_part) where delimiter is the custom delimiter
            or None if no custom delimiter, and numbers_part is the remaining string
        """
        if input_str.startswith("//"):
            # Find the newline that separates delimiter spec from numbers
            newline_pos = input_str.find("\n")
            if newline_pos != -1:
                delimiter = input_str[2:newline_pos]  # Extract delimiter after "//"
                numbers_part = input_str[newline_pos + 1:]  # Extract numbers after newline
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
            # Use custom delimiter
            number_strings = numbers_part.split(delimiter)
        else:
            # Use default delimiters (comma and/or newline)
            if "," in numbers_part or "\n" in numbers_part:
                # Replace newlines with commas to normalize delimiters
                normalized = numbers_part.replace("\n", ",")
                number_strings = normalized.split(",")
            else:
                # Single number
                number_strings = [numbers_part]

        return [int(num) for num in number_strings if num]
