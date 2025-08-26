# ruff: noqa: E402, F401
import os
import sys

from . import linear_search_itertools, linear_search_no_deps
import pytest

# current_dir = os.path.dirname(os.path.abspath(__file__))
# repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
# sys.path.append(repo_dir)
# from tools.debug_visualizer.visualize_data_structure import (
#     EdgeMetadata,
#     NodeMetadata,
#     visualize_data_structure,
# )

test_params = [
    ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
    ([1, 1, 2, 3, 3], 2),
    ([1, 2, 2, 3, 3, 4, 4], 1),
    ([1, 1, 2, 2, 3, 3, 4, 4, 5], 5),
    ([1], 1),
    ([1, 1, 2], 2),
    ([1, 2, 2], 1),
]


def test_test_inputs_all_odd_len():
    for input, _ in test_params:
        assert len(input) % 2 == 1


@pytest.mark.parametrize("test_input,expected", test_params)
def test_linear_search_itertools(test_input, expected):
    sol = linear_search_itertools.Solution()  # noqa: F841
    assert sol.singleNonDuplicate(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_linear_search_no_deps(test_input, expected):
    sol = linear_search_no_deps.Solution()  # noqa: F841
    assert sol.singleNonDuplicate(test_input) == expected
