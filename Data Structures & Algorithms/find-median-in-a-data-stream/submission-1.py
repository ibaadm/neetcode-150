class MedianFinder:

    def __init__(self):
        self.lowerHalf = [100000]
        self.upperHalf = [100000]

    def addNum(self, num: int) -> None:
        if num < -self.lowerHalf[0]:
            if len(self.lowerHalf) > len(self.upperHalf):
                heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))
            heapq.heappush(self.lowerHalf, -num)
        elif num > self.upperHalf[0]:
            if len(self.upperHalf) > len(self.lowerHalf):
                heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))
            heapq.heappush(self.upperHalf, num)
        else:
            if len(self.lowerHalf) > len(self.upperHalf):
                heapq.heappush(self.upperHalf, num)
            else:
                heapq.heappush(self.lowerHalf, -num)

    def findMedian(self) -> float:
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]
        elif len(self.upperHalf) > len(self.lowerHalf):
            return self.upperHalf[0]
        return (self.upperHalf[0] - self.lowerHalf[0]) / 2