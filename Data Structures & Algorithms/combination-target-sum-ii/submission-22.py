class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total, last_added):
            if total == target:
                res.append(subset[:])
                return

            if total > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1, total+candidates[i], True)
            subset.pop()
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, total, False)

        dfs(0, 0, False)
        return res