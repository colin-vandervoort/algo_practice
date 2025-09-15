from dataclasses import dataclass
from typing import List

import pytest

from . import min_queue


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expect: int

    def __str__(self):
        return f"kth_largest({self.nums}, {self.k}) = {self.expect}"


test_cases = [
    TestCase(nums=[], k=0, expect=0),
    TestCase(nums=[3, 2, 1, 5, 6, 4], k=2, expect=5),
    TestCase(nums=[0, 1], k=1, expect=1),
    TestCase(nums=[5, 0, 1], k=1, expect=5),
    TestCase(nums=[5, 7, 1, 2, 0], k=2, expect=5),
]


@pytest.mark.parametrize(
    "test_case", test_cases, ids=[str(test_case) for test_case in test_cases]
)
def test_kth_largest(test_case):
    assert min_queue.kth_largest(test_case.nums, test_case.k) == test_case.expect
