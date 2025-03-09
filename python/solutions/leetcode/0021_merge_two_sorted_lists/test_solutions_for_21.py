# ruff: noqa: E402, F401
import os
import sys

import iterative
import pytest
import recursive
from list_node import ListNode

# current_dir = os.path.dirname(os.path.abspath(__file__))
# repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
# sys.path.append(repo_dir)
# from tools.debug_visualizer.visualize_data_structure import (
#     EdgeMetadata,
#     NodeMetadata,
#     visualize_data_structure,
# )


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
