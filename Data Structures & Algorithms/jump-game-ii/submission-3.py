class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        steps = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            steps += 1
        return steps
