# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head

        while l1 and l1.next:
            l1 = l1.next.next
            l2 = l2.next
        l1 = head

        prev = None
        while l2:
            l2.next, l2, prev = prev, l2.next, l2
        l2 = prev

        while l1 and l2.next:
            if l1 == l2:
                break
            l1.next, l2.next, l1, l2 = l2, l1.next, l1.next, l2.next