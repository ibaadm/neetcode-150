class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        start = intervals[0][0]
        end = intervals[0][1]
        mp = defaultdict(list)
        for left, right in intervals:
            mp[left].append((left, right))
            if left < start:
                start = left
            if right > end:
                end = right

        shortest_intervals = defaultdict(lambda: -1)
        have = []
        for i in range(start, end + 1):
            for left, right in mp[i]:
                heapq.heappush(have, (right - left + 1, right))

            if have:
                shortest_intervals[i] = have[0][0]
            else:
                shortest_intervals[i] = -1

            while have and have[0][1] <= i:
                heapq.heappop(have)

        output = []
        for query in queries:
            output.append(shortest_intervals[query])
        return output
