pub struct Solution;

struct Interval {
    start: i32,
    end: i32,
}

impl From<Vec<i32>> for Interval {
    fn from(value: Vec<i32>) -> Self {
        match value.as_slice() {
            [start, end] => Interval {
                start: *start,
                end: *end,
            },
            _ => panic!(),
        }
    }
}

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut new_interval_tmp = Interval::from(new_interval.clone());

        // first, use binary search to find where the new interval will be inserted in the array
        let mut left: i32 = 0;
        let mut right: i32 = (intervals.len() - 1) as i32;

        while left <= right {
            let part = (((left + right) as f64) / 2.0).floor() as i32;
            let interval_at_partition = Interval::from(intervals[part as usize].clone());
            match new_interval_tmp.start.cmp(&(interval_at_partition.start)) {
                std::cmp::Ordering::Less => right = part - 1,
                std::cmp::Ordering::Equal => {
                    left = part;
                    break;
                }
                std::cmp::Ordering::Greater => left = part + 1,
            }
        }

        // at this point, the left index could actually be beyond an interval which overlaps the new interval
        let left_left = left - 1;

        let mut output: Vec<Vec<i32>> = if left_left >= 0 {
            let interval_left_left = Interval::from(intervals[left_left as usize].clone());
            if interval_left_left.end >= new_interval_tmp.start {
                new_interval_tmp = Interval {
                    start: std::cmp::min(new_interval_tmp.start, interval_left_left.start),
                    end: std::cmp::max(new_interval_tmp.end, interval_left_left.end),
                };
                intervals.iter().take(left_left as usize).cloned().collect()
            } else {
                intervals.iter().take(left as usize).cloned().collect()
            }
        } else {
            vec![]
        };

        // then, we move forward through the array, absorbing overlapping intervals
        for (interval_idx, interval) in intervals
            .iter()
            .enumerate()
            .skip(left as usize)
            .map(|(index, interval)| (index, Interval::from(interval.clone())))
        {
            if interval.start > new_interval_tmp.end {
                output.push(vec![new_interval_tmp.start, new_interval_tmp.end]);
                output.append(&mut intervals.iter().skip(interval_idx).cloned().collect());
                return output;
            } else {
                new_interval_tmp = Interval {
                    start: std::cmp::min(new_interval_tmp.start, interval.start),
                    end: std::cmp::max(new_interval_tmp.end, interval.end),
                }
            }
        }
        output.push(vec![new_interval_tmp.start, new_interval_tmp.end]);

        output
    }
}

pub type BinarySearchSolution = Solution;
