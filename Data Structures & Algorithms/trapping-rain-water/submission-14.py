class Solution:
    def trap(self, height: List[int]) -> int:
        level = 0
        l = 0
        r = len(height) - 1
        res = 0
        while r-l > 1:
            while r-l > 1 and height[l] - level <= 0:
                l += 1
            while r-l > 1 and height[r] - level <= 0:
                r -= 1
            for i in range(l+1, r):
                if height[i] - level <= 0:
                    res += 1
            level += 1
        return res

