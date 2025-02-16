from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        str_n = str(n)
        counter_n = Counter(str_n)
        digits_n = set(str_n)

        for exponent in range(0, 31):
            power = str(pow(2, exponent))
            counter_power = Counter(power)

            if len(digits_n ^ set(counter_power.keys())):
                continue
            if all(
                [
                    counter_n[digit_char] == counter_power[digit_char]
                    for digit_char in digits_n
                ]
            ):
                return True
        return False


solution = Solution()
print(solution.reorderedPowerOf2(512))
print(solution.reorderedPowerOf2(1521))
print(solution.reorderedPowerOf2(513))
print(solution.reorderedPowerOf2(1))
