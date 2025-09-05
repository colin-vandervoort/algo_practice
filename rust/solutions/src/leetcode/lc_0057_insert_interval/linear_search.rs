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
        let mut result: Vec<Vec<i32>> = vec![];
        let mut new_interval_tmp = Interval::from(new_interval.clone());

        for (index, interval) in intervals
            .iter()
            .enumerate()
            .map(|(index, interval)| (index, Interval::from(interval.clone())))
        {
            if new_interval_tmp.end < interval.start {
                result.push(vec![new_interval_tmp.start, new_interval_tmp.end]);
                result.append(&mut intervals.iter().skip(index).cloned().collect());
                return result;
            } else if new_interval_tmp.start > interval.end {
                result.push(vec![interval.start, interval.end]);
            } else {
                new_interval_tmp = Interval {
                    start: std::cmp::min(new_interval_tmp.start, interval.start),
                    end: std::cmp::max(new_interval_tmp.end, interval.end),
                }
            }
        }
        result.push(vec![new_interval_tmp.start, new_interval_tmp.end]);

        result
    }
}

pub type LinearSearchSolution = Solution;
