class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        q = deque()

        count = [0] * 26
        for task in tasks:
            count[ord(task)-ord('A')] += 1
        
        for i in range(26):
            if count[i]:
                heapq.heappush(heap, -count[i])

        while heap or q:
            if q and q[0][0] == time:
                _, count = q.popleft()
                heapq.heappush(heap, count)
            
            if heap:
                count = heapq.heappop(heap)
                if -count > 1:
                    q.append((time+n+1, count+1))
                time += 1
            else:
                time = q[0][0]

        return time