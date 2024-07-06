"""Module for practice in solving problems in Leetcode.com."""
from typing import List


class Solution:
    """Solution class."""

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """Solve the problem here.

        Args:
            nums (List[int]): list of numbers
            target (int): number to find the sum of 2

        Returns:
            List[int]: indexes of possible solution
        """
        heap = {}
        n = len(nums)

        for i in range(n):
            to_find = target - nums[i]
            if to_find in heap:
                return [heap[to_find], i]
            heap[nums[i]] = i

        return []  # return empty list if no solutions found


def main():
    """Execute main func."""
    print(Solution().two_sum([2, 3, 4, 5, 6], 9))


if __name__ == "__main__":
    main()
