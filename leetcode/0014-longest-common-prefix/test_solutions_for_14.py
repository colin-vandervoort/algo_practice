# ruff: noqa: E402, F401
import os
import sys

import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
repo_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(repo_dir)
import initial_approach_quadratic_complexity
import list_based_trie
import trie_fail_fast
import trie_nooby

from tools.debug_visualizer.visualize_data_structure import (
    EdgeMetadata,
    NodeMetadata,
    visualize_data_structure,
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
