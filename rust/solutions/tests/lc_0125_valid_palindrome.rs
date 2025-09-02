use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_0125_valid_palindrome::converging_iterators::ConvergingIteratorsSolution;

struct TestCase {
    string_under_test: String,
    expect: bool,
}

#[template]
#[rstest]
#[case(TestCase{string_under_test: String::from("race a car"), expect: false})]
#[case(TestCase{string_under_test: String::from("A man, a plan, a canal: Panama"), expect: true})]
#[case(TestCase{string_under_test: String::from(" "), expect: true})]
fn lc_0125_test_cases(#[case] test_case: TestCase) {}

#[apply(lc_0125_test_cases)]
fn converging_iterators(test_case: TestCase) {
    let actual = ConvergingIteratorsSolution::is_palindrome(test_case.string_under_test);
    assert_eq!(actual, test_case.expect);
}
