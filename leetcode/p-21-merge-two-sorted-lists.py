# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def next(ref_a, ref_b):
            if ref_a is None and ref_b is None:
                return None, ref_a, ref_b
            if ref_a is None:
                return ref_b, ref_a, ref_b.next
            if ref_b is None:
                return ref_a, ref_a.next, ref_b
            if ref_a.val < ref_b.val:
                return ref_a, ref_a.next, ref_b
            return ref_b, ref_a, ref_b.next
        
        ret_head, list1_pos, list2_pos = next(list1, list2)
        ret_pos = ret_head
        
        while list1_pos != None or list2_pos != None:
            next_node, list1_pos, list2_pos = next(list1_pos, list2_pos)
            ret_pos.next = next_node
            ret_pos = ret_pos.next
        
        return ret_head