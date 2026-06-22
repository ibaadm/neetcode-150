# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        curr1 = list1
        curr2 = list2
        if curr1.val > curr2.val:
            curr1, curr2 = curr2, curr1
        new_head = curr1

        while curr1.next and curr2:
            if curr1.next.val > curr2.val:
                curr1.next, curr1, curr2.next, curr2 = curr2, curr2, curr1.next, curr2.next
            else:
                curr1 = curr1.next
        if not curr1.next: curr1.next = curr2
        return new_head