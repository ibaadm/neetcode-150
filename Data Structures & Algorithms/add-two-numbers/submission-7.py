# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = ListNode(0, l1)
        curr2 = ListNode(0, l2)
        carry = 0

        while curr1.next and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next
            curr_sum = curr1.val + curr2.val + carry
            carry = curr_sum // 10
            curr1.val = curr_sum % 10

        while curr1.next:
            curr1 = curr1.next
            curr_sum = curr1.val + carry
            carry = curr_sum // 10
            curr1.val = curr_sum % 10
        
        while curr2.next:
            curr2 = curr2.next
            curr_sum = curr2.val + carry
            carry = curr_sum // 10
            curr1.next = ListNode(curr_sum % 10)
            curr1 = curr1.next

        while carry:
            curr1.next = ListNode(carry % 10)
            curr1 = curr1.next
            carry //= 10

        return l1