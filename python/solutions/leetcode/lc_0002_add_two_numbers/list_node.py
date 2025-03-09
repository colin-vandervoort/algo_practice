from typing import Optional, Self


class ListNode:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, val=0, next=None):
        """
        Initializes a new ListNode.

        Args:
            val: The value of the node.
            next: The next node in the list, or None if this is the tail.
        """
        self.val = val
        self.next = next

    def __eq__(self: Self, other: Self):
        """
        Compares two linked lists for equality.

        Args:
            other: The other linked list to compare.

        Returns:
            True if the lists are equal, False otherwise.
        """
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

    def __str__(self: Self):
        """
        Returns a string representation of the linked list.

        Returns:
            A comma-separated string of the node values.
        """
        vals = [self.val]
        pos = self
        while pos.next is not None:
            vals.append(pos.next.val)
            pos = pos.next
        return f"[{','.join(vals)}]"

    @staticmethod
    def factory(input: list) -> Optional[Self]:
        """
        Creates a linked list from a Python list.

        Args:
            input: A list of values to create the linked list from.

        Returns:
            The head of the linked list, or None if the input list is empty.
        """
        if len(input) == 0:
            return None
        output = ListNode(input[0])
        pos = output
        for val in input[1:]:
            pos.next = ListNode(val)
            pos = pos.next

        return output
