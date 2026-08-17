from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def recurse(i, t):
            if i == n:
                return t == 0
            
            return recurse(i+1, t-nums[i]) + recurse(i+1, t+nums[i])
        
        return recurse(0, target)