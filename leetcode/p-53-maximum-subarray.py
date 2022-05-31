from typing import List

# # O(N^3)
# class Solution(object):
#     def maxSubArray(self, nums: List[int]) -> int:
#         m = nums[0]
#         for r in range(len(nums)):
#             for l in range(0, r)):
#                 m = max(m, sum(nums[l:r+1]))
#         return m

# O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = nums[0]
        curr_sum = 0
        for e in nums:
            if 0 > curr_sum:
                curr_sum = 0
            curr_sum += e
            m_sum = max(m_sum, curr_sum)

        return m_sum

