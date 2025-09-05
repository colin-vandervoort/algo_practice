# Work on one category / approach strategy for a while

# Questions the question
# Identify edge cases before starting coding
#
# Identify the pattern and create a proposed solution with big O
# Walk through all cases

# k will always be less than the size of the array
# the array is unsorted
# know the underlying details of the programming language (e.g. sort implementation space complexity)
# find kth of anything -> use a heap
# go through literal examples
# with heap problems, use the size of the heap itself as a condition
# for every data structure, keep an example of how it looks at different steps
# avoid filler words, can just say "i need a little bit of time to think"
# speak slowly and clearly, each statement should convey competency
# "I'm going to use pattern X"
#   -> then provide the skeleton

# input array is [5, 7, 1, 2, 0] and k is 2
# heap [5]
# heap [5, 7]
# heap [1, 5, 7]
# heap [1, 2, 5, 7]
# heap [0, 1, 2, 5, 7]

# heap [0, 1, 2, 5]
# heap [0, 1, 2] -> 5 as result

# after coding, go through a literal example again

from typing import List
from heapq import (
    heappush,
    heappop,
    # heapify,
)

# It's worth mentioning to the interviewer that sorting the array first can
# work as part of a solution, but using a heap is often superior due to lower
# space complexity, depending on the programming language / implementation


def kth_largest(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0

    # when we declare min_heap, it is just a regular Python List,
    # but if all items are added using heapq.heappush(min_heap, x)
    # then heapq.heappop will always pop off the smallest item,
    # making it function as a min heap
    min_heap = []

    # build the heap by iterating over t
    # this can also be achieved using heapq.heapify(nums)
    # which transforms the original list into a list in-place,
    # reducing the space required by the extra list
    for elem in nums:
        heappush(min_heap, elem)

    # remove items until the top of the heap is the kth largest value
    # heapq also provides the heapq.nsmallest function which could
    # be used as part of a solution
    # while (len(min_heap) - 1) - k:
    while len(min_heap) - k:
        heappop(min_heap)

    # peek at the top of the heap
    return min_heap[0]
