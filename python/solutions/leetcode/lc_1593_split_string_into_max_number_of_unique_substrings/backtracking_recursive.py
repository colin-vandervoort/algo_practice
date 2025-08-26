class Solution:
    """
    Backtracking is usually a somewhat "brute force" approach to solving problems, so you should check to see if there are more efficient solutions.
    """

    @staticmethod
    def backtrack(s: str, start: int, seen: set) -> int:
        # base case
        if len(s) == start:
            return 0

        max_count = 0

        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)

                # add one to result of the recursion
                # this accounts for the sub string that we just chose in the current position of the call stack
                max_count = max(max_count, 1 + Solution.backtrack(s, end, seen))

                # after evaluating the current sub string and the resulting total count, remove the sub string from our "seen" set
                # this allows us to BACKTRACK and evaluate different paths which use this sub string later in the original string
                # being able to use this sub string later may result in a higher number of splits
                seen.remove(sub_string)

        return max_count

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return Solution.backtrack(s, 0, seen)


if __name__ == "__main__":
    solution = Solution()
