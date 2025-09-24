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

        # Handle single number input
        return int(numbers)
