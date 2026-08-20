from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]

        @cache
        def recurse(l, r):
            if l == r - 1:
                return 0
            
            res = 0
            for i in range(l+1, r):
                new = (
                    nums[l] * nums[i] * nums[r]
                    + recurse(l, i)
                    + recurse(i, r)
                )
                res = max(res, new)
            
            return res
        
        return recurse(0, len(nums) - 1)