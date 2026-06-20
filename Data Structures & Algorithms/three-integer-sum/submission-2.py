class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_seen = set()
        res = []
        n = len(nums)
        for i in range(n):
            fixed = nums[i]
            seen = set()
            for j in range(i+1, n):
                target = -fixed - nums[j]
                key = (min(fixed, nums[j], target), max(fixed, nums[j], target))
                if (target in seen and key not in res_seen):
                    res.append([fixed, nums[j], target])
                    res_seen.add(key)
                seen.add(nums[j])
        return res