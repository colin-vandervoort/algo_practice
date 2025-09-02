pub struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut left_iter = s
            .chars()
            .filter(|x| x.is_alphanumeric())
            .enumerate()
            .peekable();
        let mut right_iter = s
            .chars()
            .filter(|x| x.is_alphanumeric())
            .rev()
            .enumerate()
            .peekable();

        'outer: loop {
            match (left_iter.next(), right_iter.next()) {
                (None, None) => return true,
                (None, Some(_)) => return false,
                (Some(_), None) => return false,
                (Some((left_idx, left_val)), Some((right_iter_idx, right_val))) => {
                    let right_idx = s.len() - right_iter_idx - 1;
                    if left_idx >= right_idx {
                        return true;
                    }
                    if left_val.to_ascii_lowercase() == right_val.to_ascii_lowercase() {
                        continue 'outer;
                    }
                    return false;
                }
            }
        }
    }
}

pub type ConvergingIteratorsSolution = Solution;
