use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut complement_to_index_map: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for (index, value) in nums.iter().enumerate() {
            if let Ok(i32_index) = i32::try_from(index) {
                complement_to_index_map.insert(target - *value, i32_index);
            } else {
                panic!();
            };
        }
        for (index, value) in nums.iter().enumerate() {
            if let Ok(i32_index) = i32::try_from(index) {
                if let Some(complement_index) = complement_to_index_map.get(&value) {
                    if i32_index != *complement_index {
                        return vec![i32_index, *complement_index];
                    }
                }
            } else {
                panic!();
            };
        }
        vec![]
    }
}

pub type TwoPassesHashMapSolution = Solution;
