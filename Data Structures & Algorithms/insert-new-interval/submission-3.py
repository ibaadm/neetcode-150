class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        if i == n:
            res.append(newInterval)
            return res

        if intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            res += intervals[i:]
            return res

        new_start = min(intervals[i][0], newInterval[0])
        while i < n and intervals[i][0] <= newInterval[1]:
            i += 1
        
        res.append([new_start, max(newInterval[1], intervals[i-1][1])])

        if i != n:
            res += intervals[i:]
        
        return res
