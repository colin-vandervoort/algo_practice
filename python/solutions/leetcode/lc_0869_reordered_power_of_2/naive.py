from itertools import permutations


class Solution:
    POWERS_OF_TWO = {str(pow(2, k)) for k in range(0, 31)}

    def reorderedPowerOf2(self, n: int) -> bool:
        for perm in permutations(str(n)):
            if perm[0] == "0":
                continue
            reordered = "".join(perm)
            if reordered in self.POWERS_OF_TWO:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderedPowerOf2(512))
    print(solution.reorderedPowerOf2(1521))
    print(solution.reorderedPowerOf2(513))
    print(solution.reorderedPowerOf2(1))
