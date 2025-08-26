class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        longest = 0
        curr_start = 0
        for i, c in enumerate(s):
            if c not in curr_set:
                streak = i - curr_start + 1
                if streak > longest:
                    longest = streak
            while c in curr_set:
                curr_set.remove(s[curr_start])
                curr_start += 1
            curr_set.add(c)

        return longest
