pub struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: usize = 0;
        let mut right: usize = (nums.len() - 1) as usize;

        while left <= right {
            let idx_mid = (f64::from((right - left) as i32) / 2.0).floor() as usize;
            if target < nums[idx_mid] {
                right = idx_mid - 1;
            } else if nums[idx_mid] < target {
                left = idx_mid + 1;
            } else {
                return idx_mid as i32;
            }
        }
        return 0;
    }
}

pub type StandardSolution = Solution;
