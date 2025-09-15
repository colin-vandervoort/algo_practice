import pytest

from . import python_built_in_set_logic

test_params = [("abcd", "cdabcdab", 3), ("a", "aa", 2), ("a", "b", -1)]


@pytest.mark.parametrize("test_input_a, test_input_b, expected", test_params)
def test_python_built_in_set_logic(test_input_a, test_input_b, expected):
    sol = python_built_in_set_logic.Solution()  # noqa: F841
    assert sol.repeatedStringMatch(test_input_a, test_input_b) == expected
