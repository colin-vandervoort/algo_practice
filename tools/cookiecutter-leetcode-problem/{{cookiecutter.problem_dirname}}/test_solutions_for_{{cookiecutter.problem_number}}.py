import pytest

import initial_approach


test_params = []


@pytest.mark.parametrize("test_input,expected", test_params)
def test_initial_approach(test_input, expected):
    sol = initial_approach.Solution()  # noqa: F841
