pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = (nums.len() - 1) as i32;

        while left <= right {
            let idx_partition = (f64::from((right + left) as i32) / 2.0).floor() as i32;
            match target.cmp(&nums[idx_partition as usize]) {
                std::cmp::Ordering::Less => right = idx_partition - 1, // this value may be negative
                std::cmp::Ordering::Equal => return idx_partition as i32,
                std::cmp::Ordering::Greater => left = idx_partition + 1,
            }
        }
        return -1;
    }
}

pub type StandardSolution = Solution;
