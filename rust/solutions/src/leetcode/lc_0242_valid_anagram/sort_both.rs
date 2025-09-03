pub struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s = s.chars().collect::<Vec<_>>();
        let mut t = t.chars().collect::<Vec<_>>();
        s.sort_unstable();
        t.sort_unstable();
        s == t
    }
}

pub type SortBothSolution = Solution;
