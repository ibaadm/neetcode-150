class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def _combinationSum(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            for j in range(i, n):
                if total + nums[j] > target:
                    return
                
                curr.append(nums[j])
                _combinationSum(j, curr, total+nums[j])
                curr.pop()

        _combinationSum(0, [], 0)
        return res