class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = -1000
        for num in nums:
            curr = max(num, num+curr)
            res = max(res, curr)
        return res