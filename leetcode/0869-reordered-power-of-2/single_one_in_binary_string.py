from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True

        for perm in permutations(str(n)):
            if perm[0] == "0":
                continue
            if bin(int("".join(perm))).count("1") == 1:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderedPowerOf2(512))
    print(solution.reorderedPowerOf2(1521))
    print(solution.reorderedPowerOf2(513))
    print(solution.reorderedPowerOf2(1))
