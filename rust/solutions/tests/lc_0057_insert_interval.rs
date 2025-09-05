use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_0057_insert_interval::{
    binary_search::BinarySearchSolution, linear_search::LinearSearchSolution,
};

struct TestCase {
    intervals: Vec<Vec<i32>>,
    new_interval: Vec<i32>,
    expect: Vec<Vec<i32>>,
}

#[template]
#[rstest]
#[case(TestCase{
    intervals: vec![vec![2, 3], vec![6, 9]],
    new_interval: vec![0, 1],
    expect: vec![vec![0, 1], vec![2, 3], vec![6, 9]],
})]
#[case(TestCase{
    intervals: vec![vec![1, 3], vec![6, 9]],
    new_interval: vec![2, 5],
    expect: vec![vec![1, 5], vec![6, 9]],
})]
#[case(TestCase{
    intervals: vec![vec![0, 1], vec![6, 9]],
    new_interval: vec![2, 5],
    expect: vec![vec![0, 1], vec![2, 5], vec![6, 9]],
})]
#[case(TestCase{
    intervals: vec![vec![0, 1], vec![6, 9]],
    new_interval: vec![0, 2],
    expect: vec![vec![0, 2], vec![6, 9]],
})]
#[case(TestCase{
    intervals: vec![vec![1, 5]],
    new_interval: vec![6, 8],
    expect: vec![vec![1, 5], vec![6, 8]],
})]
#[case(TestCase{
    intervals: vec![vec![1, 5]],
    new_interval: vec![5, 7],
    expect: vec![vec![1, 7]],
})]
fn insert_interval_test_cases(#[case] test_case: TestCase) {}

#[apply(insert_interval_test_cases)]
fn linear_search(test_case: TestCase) {
    let actual = LinearSearchSolution::insert(test_case.intervals, test_case.new_interval);
    assert_eq!(actual, test_case.expect);
}

#[apply(insert_interval_test_cases)]
fn binary_search(test_case: TestCase) {
    let actual = BinarySearchSolution::insert(test_case.intervals, test_case.new_interval);
    assert_eq!(actual, test_case.expect);
}
