import integer_log
import naive
import pytest
import single_iteration_through_powers_of_two_basic_opt
import single_one_in_binary_string

test_params = [
    (512, True),
    (1521, False),
    (513, False),
    (1, True),
]


@pytest.mark.parametrize("test_input,expected", test_params)
def test_integer_log(test_input, expected):
    sol = integer_log.Solution()
    assert sol.reorderedPowerOf2(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_naive(test_input, expected):
    sol = naive.Solution()
    assert sol.reorderedPowerOf2(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_single_one_in_binary_string(test_input, expected):
    sol = single_one_in_binary_string.Solution()
    assert sol.reorderedPowerOf2(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_params)
def test_single_iteration_through_powers_of_two_basic_opt(test_input, expected):
    sol = single_iteration_through_powers_of_two_basic_opt.Solution()
    assert sol.reorderedPowerOf2(test_input) == expected
