class Solution:
    """
    Without backtracking, you may use a substring early on which prevents a better split later.
    """

    def maxUniqueSplit(self, s: str) -> int:
        idx_left = 0
        substrings = set()
        for idx_right in range(len(s)):
            window = s[idx_left : idx_right + 1]
            if window not in substrings:
                substrings.add(window)
                idx_left = idx_right + 1
        return len(substrings)


if __name__ == "__main__":
    solution = Solution()
