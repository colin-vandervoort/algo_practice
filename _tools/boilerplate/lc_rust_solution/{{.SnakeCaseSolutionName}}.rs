pub struct Solution;

impl Solution {
    pub fn {{ .SolutionFunctionName }}(
{{- range $_, $element := .SolutionFunctionArgs }}
{{- printf "%v: i32," $element }}
{{- end -}}
    ) -> i32 {
        0
    }
}

pub type {{ camelcase .SolutionName | printf "%vSolution" }} = Solution;
