import basic_iterative
import pytest
from list_node import ListNode as N

test_params = [
    (
        N(2, N(4, N(3))),
        N(5, N(6, N(4))),
        N(7, N(0, N(8))),
    ),
]


@pytest.mark.parametrize("list_a,list_b,expected", test_params)
def test_two_pointers(list_a, list_b, expected):
    sol = basic_iterative.Solution()
    assert sol.addTwoNumbers(list_a, list_b) == expected
