"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = Node(0)
        new_curr = new
        orig_curr = head

        count = 0
        mp = {}

        while orig_curr:
            new_curr.next = Node(orig_curr.val)
            new_curr = new_curr.next
            mp[orig_curr] = (new_curr, orig_curr.random)
            orig_curr = orig_curr.next
        
        for node, rand in mp.values():
            if rand:
                node.random = mp[rand][0]

        return new.next