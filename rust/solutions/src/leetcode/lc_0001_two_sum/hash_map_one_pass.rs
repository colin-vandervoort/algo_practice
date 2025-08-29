use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut value_to_index_map: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for (index, value) in nums.iter().enumerate() {
            if let Ok(i32_index) = i32::try_from(index) {
                let complement = target - *value;
                if let Some(complement_index) = value_to_index_map.get(&complement) {
                    return vec![*complement_index, i32_index];
                }
                value_to_index_map.insert(*value, i32_index);
            } else {
                panic!();
            };
        }
        vec![]
    }
}

pub type OnePassHashMapSolution = Solution;
