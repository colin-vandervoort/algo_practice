from heapq import heappop, heappush
from typing import Generic, List, Protocol, Self, TypeVar

T = TypeVar("T", contravariant=True)


class Comparable(Protocol[T]):
    def __lt__(self, other: T) -> bool: ...
    def __le__(self, other: T) -> bool: ...
    def __ge__(self, other: T) -> bool: ...
    def __gt__(self, other: T) -> bool: ...


ComparableType = TypeVar("ComparableType", int, float, Comparable)


class ReverseCmp(Generic[ComparableType]):
    wrapped: ComparableType

    def __init__(self, wrapped: ComparableType):
        self.wrapped = wrapped

    def __lt__(self, other: Self):
        return self.wrapped > other.wrapped

    def __le__(self, other: Self):
        return self.wrapped >= other.wrapped

    def __eq__(self, other: object):
        return self.wrapped == other

    def __ge__(self, other: Self):
        return self.wrapped <= other.wrapped

    def __gt__(self, other: Self):
        return self.wrapped < other.wrapped

    def __repr__(self) -> str:
        return repr(self.wrapped)

    def __str__(self) -> str:
        return str(self.wrapped)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap: List[ReverseCmp[int]] = []

        for elem in nums:
            heappush(max_heap, ReverseCmp(elem))

        for _ in range(k - 1):
            heappop(max_heap)

        return max_heap[0].wrapped


if __name__ == "__main__":
    solution = Solution()
