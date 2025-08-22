import re


class Solution:
    @staticmethod
    def clean_string(s: str) -> str:
        return re.sub(r"[^a-zA-Z0-9]", "", s, 0, 0).lower()

    def isPalindrome(self, s: str) -> bool:
        cleaned = Solution.clean_string(s)
        left = 0
        right = len(cleaned) - 1

        while right >= left:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
