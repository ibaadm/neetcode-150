class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_boundaries = [-1] * n
        right_boundaries = [n] * n

        for i in range(1, n):
            j = i-1
            while j > -1 and heights[j] >= heights[i]:
                j = left_boundaries[j]
            left_boundaries[i] = j

        for i in range(n-2, -1, -1):
            j = i+1
            while j < n and heights[j] >= heights[i]:
                j = right_boundaries[j]
            right_boundaries[i] = j

        res = 0
        for i, height in enumerate(heights):
            width = right_boundaries[i] - left_boundaries[i] - 1
            res = max(res, height * width)
        return res