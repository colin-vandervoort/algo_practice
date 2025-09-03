use std::collections::{HashMap, hash_map::Entry};

pub struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_hash: HashMap<char, u16> = std::collections::HashMap::new();
        for ch in s.chars() {
            s_hash
                .entry(ch)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        }
        for ch in t.chars() {
            match s_hash.entry(ch) {
                Entry::Occupied(mut occupied_entry) => {
                    let count = occupied_entry.get();
                    if *count == 0 {
                        return false;
                    } else if *count == 1 {
                        occupied_entry.remove();
                    } else {
                        occupied_entry.insert(*count - 1);
                    }
                }
                Entry::Vacant(_) => return false,
            }
        }
        s_hash.len() == 0
    }
}

pub type CharCountersSolution = Solution;
