from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        unmatched = nums[0]
        for index in range(1, len(nums), 2):
            if nums[index] == unmatched:
                unmatched = nums[index + 1]
            else:
                return unmatched

        return unmatched


if __name__ == "__main__":
    solution = Solution()
