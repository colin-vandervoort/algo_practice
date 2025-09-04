import pytest

from . import brute_force, two_pointers

test_params = [
    pytest.param(input, expect, id=f"gap({bin(input)})={expect}")
    for (input, expect) in [
        (3, 0),
        # (6, 2),
        (16, 0),
        (17, 3),
        (32, 0),
        (33, 4),
        (1162, 3),
    ]
]


@pytest.mark.parametrize("input,expected", test_params)
def test_nested_loop(input, expected):
    assert brute_force.solution(input) == expected


@pytest.mark.parametrize("input,expected", test_params)
def test_two_pointers(input, expected):
    assert two_pointers.solution(input) == expected
