from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flipped = 0
        ans = 0

        for right in range(0, len(nums)):
            if nums[right] == 0:
                flipped += 1

            if flipped > k:
                if nums[left] == 0:
                    flipped -= 1
                left += 1
            # while flipped > k:
            #     if nums[left] == 0:
            #         flipped -= 1
            #     left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()
