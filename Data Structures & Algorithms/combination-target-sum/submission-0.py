class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def _combinationSum(i):
            if i >= len(nums):
                return
            
            subtotal = sum(subset)
            num = nums[i]

            if subtotal + num <= target:
                subset.append(num)
                if subtotal + num == target:
                    res.append(subset[:])
                else:
                    _combinationSum(i)
                subset.pop()
            
            _combinationSum(i+1)
            "if its equal to target, we add to res, then we skip and continue"
            "if its less than target, we add and continue, and we skip and continue"
            "if its greater than target, we skip and continue"

        _combinationSum(0)
        return res