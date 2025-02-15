from itertools import permutations


class Solution:
    POWERS_OF_TWO = {k: pow(2, k) for k in range(1, 32)}

    def reorderedPowerOf2(self, n: int) -> bool:
        digits = [int(char) for char in str(n)]
        for perm in permutations(digits):
            if perm:
                return True
        return digits


solution = Solution()
print(solution.reorderedPowerOf2(56))
