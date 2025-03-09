import pytest

from . import basic_iterative
from .list_node import ListNode

test_params = [
    (
        ListNode.factory([2, 4, 3]),
        ListNode.factory([5, 6, 4]),
        ListNode.factory([7, 0, 8]),
    )
]


@pytest.mark.parametrize("list_a,list_b,expected", test_params)
def test_two_pointers(list_a, list_b, expected):
    sol = basic_iterative.Solution()
    assert sol.addTwoNumbers(list_a, list_b) == expected
