pub struct Solution;

impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        let x_dist = (z - x).abs();
        let y_dist = (z - y).abs();
        match x_dist.cmp(&y_dist) {
            std::cmp::Ordering::Less => 1,
            std::cmp::Ordering::Equal => 0,
            std::cmp::Ordering::Greater => 2,
        }
    }
}

pub type InitialApproachSolution = Solution;
