class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        sorted_nums = sorted(candidates)

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            
            for j in range(i, n):
                num = sorted_nums[j]
                if j > i and num == sorted_nums[j-1]:
                    continue
                
                if total + num > target:
                    return
                
                curr.append(num)
                dfs(j+1, curr, total + num)
                curr.pop()
        
        dfs(0, [], 0)
        return res