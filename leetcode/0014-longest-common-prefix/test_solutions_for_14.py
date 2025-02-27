import pytest

import initial_approach_quadratic_complexity
import trie_fail_fast
import trie_nooby


test_params = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["", "b"], ""),
]


@pytest.mark.parametrize("test_input,expected", test_params)
def test_initial_approach(test_input, expected):
    sol = initial_approach_quadratic_complexity.Solution()  # noqa: F841
    assert sol.longestCommonPrefix(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_trie_nooby(test_input, expected):
    sol = trie_nooby.Solution()  # noqa: F841
    assert sol.longestCommonPrefix(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_trie_fail_fast(test_input, expected):
    sol = trie_fail_fast.Solution()  # noqa: F841
    assert sol.longestCommonPrefix(test_input) == expected
