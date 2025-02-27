from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_len = 0
        longest_common_prefix = ""
        common_prefix_under_test = ""
        while True:
            if any([len(str_under_test) == prefix_len for str_under_test in strs]):
                return longest_common_prefix
            common_prefix_under_test = strs[0][0 : prefix_len + 1]
            for str_under_test in strs[1:]:
                if str_under_test[0 : prefix_len + 1] != common_prefix_under_test:
                    return longest_common_prefix
            longest_common_prefix = common_prefix_under_test
            prefix_len += 1


if __name__ == "__main__":
    solution = Solution()
