from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if (total & 1) == 1:
            return False
        
        n = len(nums)

        @cache
        def recurse(i, target):
            if target == 0:
                return True
            
            if i == n:
                return False
            
            return recurse(i+1, target - nums[i]) or recurse(i+1, target)
        
        return recurse(0, total // 2)