class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []

        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                res = max(res, h*w)
            stack.append(i)
        return res