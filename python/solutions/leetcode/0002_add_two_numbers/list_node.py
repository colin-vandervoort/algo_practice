from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self: Self, other: Self):
        if self.val != other.val:
            return False
        if self.next is None:
            if other.next is None:
                return True
            else:
                return False
        else:
            if other.next is None:
                return False
            else:
                return self.next == other.next
