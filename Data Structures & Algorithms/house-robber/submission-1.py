class Solution:
    def rob(self, nums: List[int]) -> int:
        no_rob = 0
        rob = 0

        for num in nums:
            rob, no_rob = num + no_rob, max(rob, no_rob)
            
        return max(rob, no_rob)
