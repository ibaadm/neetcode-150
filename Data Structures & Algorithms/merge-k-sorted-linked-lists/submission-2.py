import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        dummy = curr = ListNode()
        while heap:
            _, i, l = heapq.heappop(heap)
            curr.next = l
            curr = curr.next
            next = l.next
            if next:
                heapq.heappush(heap, (next.val, i, next))
        return dummy.next
        