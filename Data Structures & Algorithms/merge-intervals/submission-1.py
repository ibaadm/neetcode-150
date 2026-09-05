class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []

        i = 0
        while True:
            start = intervals[i][0]
            end = intervals[i][1]

            i += 1
            while i < n and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1

            res.append([start, end])

            if i == n:
                break
        
        return res