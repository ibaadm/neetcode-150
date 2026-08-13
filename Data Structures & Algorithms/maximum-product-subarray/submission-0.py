class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max_prod = min_prod = nums[0]
        for i in range(1, len(nums)):
            new = nums[i]
            from_max = max_prod * new
            from_min = min_prod * new
            max_prod = max(new, from_max, from_min)
            min_prod = min(new, from_max, from_min)
            res = max(res, max_prod)
        return res
