// cspell: ignore validparentheses

package lc0020validparentheses

import (
	"reflect"
	"testing"
)

type ValidParenthesesTestCase struct {
	input  string
	expect bool
}

var testCases = []ValidParenthesesTestCase{
	{"(]", false},
	{"()", true},
}

func isValid(s string) bool {
	var stack []rune
	stack = make([]rune, 0, 10000)

	for _, char := range s {
		switch char {
		case '(', '[', '{':
			stack = append(stack, char)
		case ')':
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] == '(' {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		case ']':
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] == '[' {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		case '}':
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] == '{' {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

func TestIsValid(t *testing.T) {
	for _, testCase := range testCases {
		actual := isValid(testCase.input)
		if !reflect.DeepEqual(actual, testCase.expect) {
			t.Errorf("isValid(\"%v\") = %v; expect %v", testCase.input, actual, testCase.expect)
		}
	}
}
