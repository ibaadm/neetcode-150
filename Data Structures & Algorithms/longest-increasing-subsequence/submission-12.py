from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def recurse(i):
            best = 0
            curr = nums[i]
            smallest_call = 1001
            for j in range(i+1, n):
                if nums[j] > curr and nums[j] < smallest_call:
                    best = max(best, recurse(j))
            return 1 + best

        return max(recurse(i) for i in range(n))
