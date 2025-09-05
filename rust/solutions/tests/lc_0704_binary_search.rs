use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_0704_binary_search::standard::StandardSolution;

struct TestCase {
    nums: Vec<i32>,
    target: i32,
    expect: i32,
}

#[template]
#[rstest]
#[case(TestCase{nums: vec![-1,0,3,5,9,12], target: 9, expect: 4})]
#[case(TestCase{nums: vec![-1,0,3,5,9,12], target: 2, expect: -1})]
#[case(TestCase{nums: vec![5], target: -5, expect: -1})]
#[case(TestCase{nums: vec![5], target: 5, expect: 0})]
fn lc_0001_test_cases(#[case] test_case: TestCase) {}

#[apply(lc_0001_test_cases)]
fn standard(test_case: TestCase) {
    let actual = StandardSolution::search(test_case.nums, test_case.target);
    assert_eq!(actual, test_case.expect)
}
