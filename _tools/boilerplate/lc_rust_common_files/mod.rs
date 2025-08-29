{{ range $_, $element := .SolutionNames }}
pub mod {{ $element }};
{{ end }}
