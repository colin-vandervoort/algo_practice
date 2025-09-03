// cSpell: ignore nagaram

use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_0242_valid_anagram::{
    char_counters::CharCountersSolution, sort_both::SortBothSolution,
};

struct TestCase {
    string_a: String,
    string_b: String,
    expect: bool,
}

#[template]
#[rstest]
#[case(TestCase{string_a: String::from("anagram"), string_b: String::from("nagaram"), expect: true})]
#[case(TestCase{string_a: String::from("ab"), string_b: String::from("a"), expect: false})]
fn lc_0242_test_cases(#[case] test_case: TestCase) {}

#[apply(lc_0242_test_cases)]
fn is_anagram(test_case: TestCase) {
    let actual = SortBothSolution::is_anagram(test_case.string_a, test_case.string_b);
    assert_eq!(actual, test_case.expect);
}

#[apply(lc_0242_test_cases)]
fn char_counters(test_case: TestCase) {
    let actual = CharCountersSolution::is_anagram(test_case.string_a, test_case.string_b);
    assert_eq!(actual, test_case.expect);
}
