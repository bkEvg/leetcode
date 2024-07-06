"""Module for practice in solving problems in Leetcode.com."""


class Solution:
    """Solution class."""

    def is_palindrome(self, x: int) -> bool:
        """Solve the problem here."""
        copy = x
        reversed_num = ''
        # only positive integers can be palindrome
        while x > 0:
            last_digit = x % 10
            x //= 10
            reversed_num += str(last_digit)

        if reversed_num == str(copy):
            return True
        return False


def main():
    """Execute main func."""
    print(Solution().is_palindrome(-121))


if __name__ == "__main__":
    main()
