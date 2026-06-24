class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [(temperatures[-1], n-1)]
        for i in range(n-2, -1, -1):
            temp = temperatures[i]
            while stack and temp >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
        return res