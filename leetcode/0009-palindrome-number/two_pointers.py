class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        idx_left = 0
        idx_right = len(x_str) - 1
        while True:
            if idx_left > idx_right:
                return True

            if x_str[idx_left] != x_str[idx_right]:
                return False

            idx_left += 1
            idx_right -= 1
