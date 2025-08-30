pub struct Solution;

impl Solution {
}

pub type {{ camelcase .SolutionName | printf "%vSolution" }} = Solution;
