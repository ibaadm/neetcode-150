# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_camp = None
        scout = head
        curr = head
        res = None
        while scout:
            camp = scout
            for _ in range(k):
                if not scout:
                    prev_camp.next = camp
                    return res
                scout = scout.next
            prev = None
            while curr is not scout:
                curr.next, curr, prev = prev, curr.next, curr
            if not res:
                res = prev
            else:
                prev_camp.next = prev
            prev_camp = camp
        return res