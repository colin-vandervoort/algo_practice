# ruff: noqa: E402, F401
import os
import sys

import iterative
import pytest
import recursive

current_dir = os.path.dirname(os.path.abspath(__file__))
repo_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(repo_dir)
from tools.debug_visualizer.visualize_data_structure import (
    EdgeMetadata, NodeMetadata, visualize_data_structure)

test_params = []


@pytest.mark.parametrize("test_input,expected", test_params)
def test_iterative(test_input, expected):
    sol = iterative.Solution()  # noqa: F841


@pytest.mark.parametrize("test_input,expected", test_params)
def test_recursive(test_input, expected):
    sol = recursive.Solution()  # noqa: F841
