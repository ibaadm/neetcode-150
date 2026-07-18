class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def _permute(curr, picked):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    _permute(curr, picked)
                    curr.pop()
                    picked[i] = False
        
        _permute([], [False] * n)
        return res
"""
we have our current list so far
for each recursion, we add every element that has not been added
yet one at a time and recurse on that, then pop it then boom
"""