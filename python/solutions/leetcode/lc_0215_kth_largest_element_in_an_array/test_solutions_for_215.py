from dataclasses import dataclass
from typing import List

import pytest

from . import max_heap, min_heap


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expect: int


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


@pytest.mark.parametrize("test_case", test_cases)
def test_min_heap(test_case):
    sol = min_heap.Solution()
    assert sol.findKthLargest(test_case.nums, test_case.k) == test_case.expect


@pytest.mark.parametrize("test_case", test_cases)
def test_max_heap(test_case):
    sol = max_heap.Solution()
    assert sol.findKthLargest(test_case.nums, test_case.k) == test_case.expect
