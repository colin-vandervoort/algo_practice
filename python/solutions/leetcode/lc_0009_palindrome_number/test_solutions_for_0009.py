import pytest

from . import two_pointers

test_params = [
    (0, True),
    (1, True),
    (11, True),
    (121, True),
    (1221, True),
    (1231, False),
]


@pytest.mark.parametrize("test_input,expected", test_params)
def test_two_pointers(test_input, expected):
    sol = two_pointers.Solution()
    assert sol.isPalindrome(test_input) == expected
