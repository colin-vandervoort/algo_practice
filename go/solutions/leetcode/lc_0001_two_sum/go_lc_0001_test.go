package main

import (
	"reflect"
	"testing"

	hash_map_one_pass "github.com/colin-vandervoort/algo_practice/go/solutions/leetcode/lc_0001_two_sum/hash_map_one_pass"
	hash_map_two_pass "github.com/colin-vandervoort/algo_practice/go/solutions/leetcode/lc_0001_two_sum/hash_map_two_pass"
)

type TwoSumSolution func([]int, int) []int

type TwoSumTestCase struct {
	nums   []int
	target int
	expect []int
}

var testCases = []TwoSumTestCase{
	{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
	{[]int{3, 2, 4}, 6, []int{1, 2}},
	{[]int{3, 3}, 6, []int{0, 1}},
}

func testHelper(t *testing.T, solution TwoSumSolution) {
	for _, testCase := range testCases {
		actual := solution(testCase.nums, testCase.target)
		if !reflect.DeepEqual(actual, testCase.expect) {
			t.Errorf("twoSum(%v, %d) = %v; expect %v", testCase.nums, testCase.target, actual, testCase.expect)
		}
	}
}

func TestDiffMapOnePass(t *testing.T) {
	testHelper(t, hash_map_one_pass.TwoSum)
}

func TestDiffMapTwoPass(t *testing.T) {
	testHelper(t, hash_map_two_pass.TwoSum)
}
