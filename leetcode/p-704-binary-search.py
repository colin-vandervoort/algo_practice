class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lower = 0
        upper = len(nums) - 1

        while True:
            part = (lower + upper) // 2
            if target == nums[part]:
                return part
            elif lower == part:
                if nums[upper] == target:
                    return upper
                return -1
            elif target < nums[part]:
                upper = part
            else:
                lower = part

