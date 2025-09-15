# ruff: noqa: E402, F401

import pytest

from . import (
    backtracking_recursive,
    backtracking_recursive_with_pruning,
    sliding_window_with_histogram,
)

test_params = [
    ("ababccc", 5),
    ("aba", 2),
    ("aa", 1),
    # wwwzfvedwfvhsww
    # w, ww, z, f, v, e, d, wf, vh, sww     (max_count: 10 - not optimal)
    # ww, w, z, f, v, e, d, wf, vh, sww     (max_count: 10 - not optimal)
    # www,   z, f, v, e, d, w, fv, h, s, ww (max_count: 11 - optimal, we get to use "w", "ww", and "www")
    ("wwwzfvedwfvhsww", 11),
]


# @pytest.mark.parametrize("test_input,expected", test_params)
# def test_sliding_window_with_histogram(test_input, expected):
#     sol = sliding_window_with_histogram.Solution()
#     assert sol.maxUniqueSplit(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_backtracking_recursive(test_input, expected):
    sol = backtracking_recursive.Solution()
    assert sol.maxUniqueSplit(test_input) == expected


# @pytest.mark.parametrize("test_input,expected", test_params)
# def test_backtracking_recursive_with_pruning(test_input, expected):
#     sol = backtracking_recursive_with_pruning.Solution()
#     assert sol.maxUniqueSplit(test_input) == expected
