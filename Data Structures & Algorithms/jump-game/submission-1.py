class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()

        def dfs(i):
            if nums[i] >= n - i - 1:
                return True
            
            for j in range(nums[i], 0, -1):
                if i + j in visited:
                    continue
                if dfs(i + j):
                    return True
                visited.add(i + j)
            
            return False
        
        return dfs(0)