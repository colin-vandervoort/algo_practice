from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # b is the possible substring and a is what we need to repeat in order to contain b
        # take q to be the ratio of len(b) to len(a), rounded up
        # this initial value for q is returned if a * q contains b
        # otherwise, we need to repeat a one more time for b to potentially be a substring
        q = ceil(len(b) / len(a))
        for i in range(2):
            if b in a * (q + i):
                return q + i
        return -1


if __name__ == "__main__":
    solution = Solution()
