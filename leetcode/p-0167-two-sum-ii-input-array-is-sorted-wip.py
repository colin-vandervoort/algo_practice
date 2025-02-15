class Solution:
    def binarySearch(self, haystack: List[int], needle: int) -> int:
        left, right = 0, len(haystack) - 1
        while left < right:
            mid = left + (right - left) // 2
            if haystack[mid] > needle:
                right = mid
            else:
                left = mid + 1
        return left + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, a in enumerate(numbers):
            needle_offset = self.binarySearch(numbers[i + 1 :], target - a)
            b = numbers[i + needle_offset]
            if a + b == target:
                return [i + 1, i + needle_offset]
