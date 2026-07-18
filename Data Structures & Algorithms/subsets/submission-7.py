class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def _subsets(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            _subsets(i+1)
            subset.append(nums[i])
            _subsets(i+1)
            subset.pop()
        
        _subsets(0)
        return res