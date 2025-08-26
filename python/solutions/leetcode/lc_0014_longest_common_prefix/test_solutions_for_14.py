import pytest

from . import (
    initial_approach_quadratic_complexity,
    list_based_trie,
    trie_fail_fast,
    trie_nooby,
)

test_params = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["", "b"], ""),
    (["a"], "a"),
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


@pytest.mark.parametrize("test_input,expected", test_params)
def test_list_based_trie(test_input, expected):
    # def visualizer_node_mapper(ds):
    #     # use id() for unique object ids
    sol = list_based_trie.Solution()  # noqa: F841
    assert sol.longestCommonPrefix(test_input) == expected
