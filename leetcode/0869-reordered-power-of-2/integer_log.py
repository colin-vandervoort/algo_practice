from itertools import permutations
from math import isclose, log2


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True

        for perm in permutations(str(n)):
            if perm[0] == "0":
                continue
            if int(perm[-1]) & 1:
                continue
            result_num = int("".join(perm))
            result_log_2 = log2(result_num)
            result_log_2_rounded = round(result_log_2, 0)
            if isclose(result_log_2, result_log_2_rounded):
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderedPowerOf2(512))
    print(solution.reorderedPowerOf2(1521))
    print(solution.reorderedPowerOf2(513))
    print(solution.reorderedPowerOf2(1))
