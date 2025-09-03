{{- $snakeCaseProblemName := snakecase .ProblemName -}}
{{- $solutionFunctionName := .SolutionFunctionName -}}
{{- $solutionFunctionArgs := .SolutionFunctionArgs -}}
{{- $solutionModuleNames := list -}}
{{- range $element := .SolutionNames -}}
	{{ $snakeCaseName := snakecase $element -}}
	{{ $solutionModuleNames = append $solutionModuleNames $snakeCaseName -}}
{{- end -}}

use rstest::rstest;
use rstest_reuse::*;

use solutions::leetcode::{{ printf "lc_%04d_%v" .ProblemNumber $snakeCaseProblemName }}::{
{{- range $_, $element := .SolutionNames }}
    {{ $element | snakecase }}::{{ $element | camelcase -}}Solution,
{{- end }}
};

struct TestCase {
{{- range $_, $element := $solutionFunctionArgs }}
    {{ $element }}: i32,
{{- end }}
    expect: i32,
}

#[template]
#[rstest]
{{ "#[case(TestCase{" }}
{{- range $_, $element := $solutionFunctionArgs }}
    {{ $element }}: 0,
{{- end }}
    expect: 0
{{ "})]" }}
fn {{ $snakeCaseProblemName }}_test_cases(#[case] test_case: TestCase) {}

{{ range $_, $element := .SolutionNames -}}
#[apply({{ $snakeCaseProblemName }}_test_cases)]
fn {{ snakecase $element }}(test_case: TestCase) {
    let actual = {{ camelcase $element }}Solution::{{ $solutionFunctionName }}(
{{ range $_, $element := $solutionFunctionArgs -}}
{{ printf "test_case.%v," $element }}
{{ end -}}
    );
    assert_eq!(actual, test_case.expect);
}
{{ end }}
