# ruff: noqa: E402, F401
import os
import sys

import pytest

from . import sliding_window

# current_dir = os.path.dirname(os.path.abspath(__file__))
# repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
# sys.path.append(repo_dir)
# from tools.debug_visualizer.visualize_data_structure import (
#     EdgeMetadata,
#     NodeMetadata,
#     visualize_data_structure,
# )

test_params = [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
]


@pytest.mark.parametrize("input_array,input_k,expected", test_params)
def test_sliding_window(input_array, input_k, expected):
    sol = sliding_window.Solution()  # noqa: F841
    assert sol.longestOnes(input_array, input_k) == expected
