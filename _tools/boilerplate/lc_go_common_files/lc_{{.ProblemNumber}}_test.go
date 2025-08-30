//lint:file-ignore U1000 Ignore all unused code, it's generated
//go:build ignore
{{ $problemDirectory := .ProblemDirectory -}}
{{- $snakeCaseSolutionNames := list -}}
{{- range $element := .SolutionNames -}}
	{{ $snakeCaseName := snakecase $element -}}
	{{ $snakeCaseSolutionNames = append $snakeCaseSolutionNames $snakeCaseName -}}
{{- end }}
package main

import (
	"reflect"
	"testing"

	{{ range $_, $element := $snakeCaseSolutionNames }}{{printf "%v \"github.com/colin-vandervoort/algo_practice/go/solutions/leetcode/%v/%v\"" $element $problemDirectory $element }}{{ end }}
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
