class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n-2, -1, -1):
            j = i+1
            while res[j] and temperatures[j] <= temperatures[i]:
                j += res[j]
            if temperatures[j] > temperatures[i]:
                res[i] = j-i
            else:
                res[i] = 0
        return res
