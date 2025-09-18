from dataclasses import dataclass
from typing import List

import pytest

from . import max_heap, min_heap_in_place, min_heap_pure


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expect: int

    def __str__(self):
        nums_preview = (
            str(self.nums)
            if len(self.nums) < 5
            else f"[{self.nums[0]}, {self.nums[1]}, {self.nums[2]}, ...]"
        )
        return f"nums={nums_preview}, k={self.k}"


def idfn(val):
    if isinstance(val, TestCase):
        return str(val)


test_cases = [
    TestCase(nums=[0], k=1, expect=0),
    TestCase(nums=[3, 2, 1, 5, 6, 4], k=2, expect=5),
    TestCase(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4, expect=4),
]


def test_parameters_valid():
    for test_case in test_cases:
        assert 1 <= test_case.k
        assert test_case.k <= pow(10, 5)

        assert 1 <= len(test_case.nums)
        assert len(test_case.nums) <= pow(10, 5)

        for n in test_case.nums:
            assert -pow(10, 4) <= n
            assert n <= pow(10, 4)


@pytest.mark.parametrize("test_case", test_cases, ids=idfn)
def test_min_heap_in_place(test_case):
    sol = min_heap_in_place.Solution()
    assert sol.findKthLargest(test_case.nums, test_case.k) == test_case.expect


@pytest.mark.parametrize("test_case", test_cases, ids=idfn)
def test_min_heap_pure(test_case):
    sol = min_heap_pure.Solution()
    assert sol.findKthLargest(test_case.nums, test_case.k) == test_case.expect


@pytest.mark.parametrize("test_case", test_cases, ids=idfn)
def test_max_heap(test_case):
    sol = max_heap.Solution()
    assert sol.findKthLargest(test_case.nums, test_case.k) == test_case.expect
