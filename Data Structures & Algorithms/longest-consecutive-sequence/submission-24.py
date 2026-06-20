from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        consecutivities = defaultdict(int)
        for num in nums:
            if consecutivities[num] != 0:
                continue
            right = consecutivities[num+1]
            left = consecutivities[num-1]
            curr = right + left + 1
            consecutivities[num] = curr
            consecutivities[num+right] = curr
            consecutivities[num-left] = curr
            res = max(res, curr)

        return res
