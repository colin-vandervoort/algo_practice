# ruff: noqa: E402, F401
import os
import sys

import pytest

from . import sliding_window

solution_test_params = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
]


@pytest.mark.parametrize("test_input,expected", solution_test_params)
def test_sliding_window(test_input, expected):
    sol = sliding_window.Solution()  # noqa: F841
    assert sol.isPalindrome(test_input) == expected


# Helper functions

clean_func_test_params = [
    ("A man, a plan, a canal: Panama", "amanaplanacanalpanama"),
    ("race a car", "raceacar"),
    (" ", ""),
]


@pytest.mark.parametrize("test_input,expected", clean_func_test_params)
def test_clean_func(test_input, expected):
    assert sliding_window.Solution.clean_string(test_input) == expected
