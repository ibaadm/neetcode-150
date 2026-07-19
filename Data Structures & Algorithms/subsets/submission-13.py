class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(i, curr):
            res.append(curr[:])            
            for j in range(i, n):
                curr.append(nums[j])
                dfs(j+1, curr)
                curr.pop()
        
        dfs(0, [])
        return res
