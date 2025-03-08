# Definition for singly-linked list.
from typing import Optional

from list_node import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum = None
        sum_prev_position = None
        carry = 0

        while l1 is not None or l2 is not None:
            position_sum = carry
            if l1 is not None:
                position_sum += l1.val
            if l2 is not None:
                position_sum += l2.val
            carry = 1 if position_sum > 9 else 0

            new_node = ListNode(
                (position_sum - 10 if position_sum > 9 else position_sum), None
            )

            if sum is None:
                sum = new_node
                sum_prev_position = sum
            else:
                sum_prev_position.next = new_node
                sum_prev_position = new_node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry != 0:
            sum_prev_position.next = ListNode(1, None)

        return sum
