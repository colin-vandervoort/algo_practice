{{ range $_, $element := .SolutionNames }}pub mod {{ snakecase $element }};{{ end }}
