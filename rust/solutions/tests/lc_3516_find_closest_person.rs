use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::lc_3516_find_closest_person::initial_approach::InitialApproachSolution;

struct TestCase {
    x: i32,
    y: i32,
    z: i32,
    expect: i32,
}

#[template]
#[rstest]
#[case(TestCase{
    x: 2,
    y: 7,
    z: 4,
    expect: 1
})]
#[case(TestCase{
    x: 2,
    y: 5,
    z: 4,
    expect: 2
})]
#[case(TestCase{
    x: 1,
    y: 5,
    z: 3,
    expect: 0
})]
fn find_closest_person_test_cases(#[case] test_case: TestCase) {}

#[apply(find_closest_person_test_cases)]
fn initial_approach(test_case: TestCase) {
    let actual = InitialApproachSolution::find_closest(test_case.x, test_case.y, test_case.z);
    assert_eq!(actual, test_case.expect);
}
