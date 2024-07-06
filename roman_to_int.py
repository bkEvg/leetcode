"""Module for practice in solving problems in Leetcode.com."""


class Solution:
    """Solution class."""

    def roman_to_int(self, s: str) -> int:
        """Solve the problem here."""
        roma_to_arabic: dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result: int = 0
        last_value = roma_to_arabic[s[0]]
        for char in s:
            current_value = roma_to_arabic[char]
            if current_value <= last_value:
                result += current_value
                last_value = current_value
            else:
                result = result - last_value + (current_value - last_value)

        return result


def main():
    """Execute main func."""
    print(Solution().roman_to_int("MCMXCIV"))


if __name__ == "__main__":
    main()
