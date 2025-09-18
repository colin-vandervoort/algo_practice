from heapq import heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            heappush(min_heap, n)

        while len(min_heap) - k:
            heappop(min_heap)

        return min_heap[0]


if __name__ == "__main__":
    solution = Solution()
