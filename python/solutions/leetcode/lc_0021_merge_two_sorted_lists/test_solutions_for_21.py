import pytest

from . import iterative, recursive
from .list_node import ListNode


def get_test_params():
    return [
        (
            ListNode.factory([1, 2, 4]),
            ListNode.factory([1, 3, 4]),
            ListNode.factory([1, 1, 2, 3, 4, 4]),
        ),
        (
            ListNode.factory([-1, 2, 8]),
            ListNode.factory([9]),
            ListNode.factory([-1, 2, 8, 9]),
        ),
    ]


@pytest.mark.parametrize("list_a,list_b,expected", get_test_params())
def test_iterative(list_a, list_b, expected):
    sol = iterative.Solution()
    assert sol.mergeTwoLists(list_a, list_b) == expected


@pytest.mark.parametrize("list_a,list_b,expected", get_test_params())
def test_recursive(list_a, list_b, expected):
    sol = recursive.Solution()
    actual = sol.mergeTwoLists(list_a, list_b)
    assert actual == expected
