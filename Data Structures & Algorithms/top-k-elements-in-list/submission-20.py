from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sorted_counts = [[] for _ in range(n+1)]
        for x, f in Counter(nums).items():
            sorted_counts[f].append(x)
        res = []
        i = n
        while True:
            if len(res) == k:
                return res
            for x in sorted_counts[i]:
                res.append(x)
            i -= 1