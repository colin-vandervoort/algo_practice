import pytest

from . import sliding_window_with_histogram

test_params = [
    ("ababccc", 5),
    ("aba", 2),
    ("aa", 1),
]


@pytest.mark.parametrize("test_input,expected", test_params)
def test_sliding_window_with_histogram(test_input, expected):
    sol = sliding_window_with_histogram.Solution()
    assert sol.maxUniqueSplit(test_input) == expected
