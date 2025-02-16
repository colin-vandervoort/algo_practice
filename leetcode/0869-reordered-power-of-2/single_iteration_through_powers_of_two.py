from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter_n = Counter(str(n))

        for exponent in range(0, 31):
            power = str(pow(2, exponent))
            counter_power = Counter(power)

            if all([counter_n[str(i)] == counter_power[str(i)] for i in range(0, 10)]):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderedPowerOf2(512))
    print(solution.reorderedPowerOf2(1521))
    print(solution.reorderedPowerOf2(513))
    print(solution.reorderedPowerOf2(1))
