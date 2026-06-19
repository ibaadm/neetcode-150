from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(Counter(nums).items())
        return [n for n, _ in sorted(counts, reverse=True, key=lambda x: x[1])][:k]
        