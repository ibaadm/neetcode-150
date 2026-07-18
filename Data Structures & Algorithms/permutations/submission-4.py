class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def _permute(curr, picked, res):
            if len(curr) == n:
                res.append(curr[:])
                return

            for i in range(n):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    _permute(curr, picked, res)
                    curr.pop()
                    picked[i] = False
        
        _permute([], [False] * n, res)
        return res