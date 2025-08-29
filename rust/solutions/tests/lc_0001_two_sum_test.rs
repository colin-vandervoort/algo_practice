use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_0001_two_sum::{
    hash_map_one_pass::OnePassHashMapSolution, hash_map_two_passes::TwoPassesHashMapSolution,
};

struct TestCase {
    nums: Vec<i32>,
    sum: i32,
    expect: Vec<i32>,
}

#[template]
#[rstest]
#[case(TestCase{nums: [2, 7, 11, 15].to_vec(), sum: 9, expect: [0, 1].to_vec()})]
#[case(TestCase{nums: [3, 2, 4].to_vec(), sum: 6, expect: [1, 2].to_vec()})]
#[case(TestCase{nums: [1, 2].to_vec(), sum: 3, expect: [0, 1].to_vec()})]
fn lc_0001_test_cases(#[case] test_case: TestCase) {}

#[apply(lc_0001_test_cases)]
fn hash_map_one_pass(test_case: TestCase) {
    let actual = OnePassHashMapSolution::two_sum(test_case.nums, test_case.sum);
    assert_eq!(actual, test_case.expect)
}

#[apply(lc_0001_test_cases)]
fn hash_map_two_passes(test_case: TestCase) {
    let actual = TwoPassesHashMapSolution::two_sum(test_case.nums, test_case.sum);
    assert_eq!(actual, test_case.expect)
}
