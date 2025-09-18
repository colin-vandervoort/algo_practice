import heapq

from . import max_heap


def test_reverse_cmp_int_eq():
    rev_cmp_1_a = max_heap.ReverseCmp[int](1)
    rev_cmp_1_b = max_heap.ReverseCmp[int](1)

    assert rev_cmp_1_a == rev_cmp_1_b


def test_reverse_cmp_int_gt():
    rev_cmp_1 = max_heap.ReverseCmp[int](1)
    rev_cmp_2 = max_heap.ReverseCmp[int](2)

    assert rev_cmp_1 > rev_cmp_2


def test_reverse_cmp_float_gt():
    rev_cmp_1 = max_heap.ReverseCmp[float](1.0)
    rev_cmp_2 = max_heap.ReverseCmp[float](2.0)

    assert rev_cmp_1 > rev_cmp_2


def test_max_heap():
    nums = [max_heap.ReverseCmp(num) for num in [2, 5, 1]]

    heapq.heapify(nums)

    assert nums[0] == 5
