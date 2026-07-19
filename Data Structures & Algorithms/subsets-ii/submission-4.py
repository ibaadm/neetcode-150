class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        def dfs(i, curr):
            res.append(curr[:])
            for j in range(i, n):
                if j > i and sorted_nums[j] == sorted_nums[j-1]:
                    continue
                curr.append(sorted_nums[j])
                dfs(j+1, curr)
                curr.pop()

        dfs(0, [])
        return res