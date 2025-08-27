from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        list_len = len(nums)

        # base case
        if list_len == 1:
            return nums[0]
        if list_len == 3:
            # two of these values are the same
            # and will XOR each other out
            return nums[0] ^ nums[1] ^ nums[2]

        idx_center = list_len // 2
        idx_center_left = idx_center - 1
        idx_center_right = idx_center + 1
        if (
            nums[idx_center_left] != nums[idx_center]
            and nums[idx_center] != nums[idx_center_right]
        ):
            # if there are no pairs in the middle three elements,
            # then the middle element can't have a match
            return nums[idx_center]

        # recursive step
        (left_partition, right_partition) = (
            (nums[:idx_center_left], nums[idx_center_right:])
            if nums[idx_center_left] == nums[idx_center]
            else (
                nums[:idx_center],
                nums[idx_center_right + 1 :],
            )
        )
        # the partition with an odd number of elements must have the unmatched item
        if len(left_partition) % 2:
            return self.singleNonDuplicate(left_partition)
        else:
            return self.singleNonDuplicate(right_partition)
