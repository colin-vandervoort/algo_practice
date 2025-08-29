//lint:file-ignore U1000 Ignore all unused code, it's generated

package main

import (
	"reflect"
	"testing"
)

type Solution func([]int) int

type TestCase struct {
	inputA []int
	expect int
}

var testCases = []TestCase{}

func testHelper(t *testing.T, solution Solution) {
	for _, testCase := range testCases {
		actual := solution(testCase.inputA)
		if !reflect.DeepEqual(actual, testCase.expect) {
			t.Errorf("solution(%v) = %v; expect %v", testCase.inputA, actual, testCase.expect)
		}
	}
}
