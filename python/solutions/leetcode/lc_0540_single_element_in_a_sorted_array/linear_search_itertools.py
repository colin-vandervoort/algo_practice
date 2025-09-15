# cspell: ignore BCDE, CDEF, DEFG

# from collections import deque
from itertools import batched  # islice,
from typing import List


class Solution:
    # @staticmethod
    # def sliding_window(iterable, n):
    #     "Collect data into overlapping fixed-length chunks or blocks."
    #     # sliding_window("ABCDEFG", 4) → "ABCD" "BCDE" "CDEF" "DEFG"
    #     iterator = iter(iterable)
    #     window = deque(islice(iterator, n - 1), maxlen=n)
    #     for x in iterator:
    #         window.append(x)
    #         yield tuple(window)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        unmatched = nums[0]
        for e0, e1 in batched(nums[1:], 2):
            if unmatched != e0:
                return unmatched
            else:
                unmatched = e1

        return unmatched


if __name__ == "__main__":
    solution = Solution()
