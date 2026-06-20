class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        consecutivities = {}
        for num in nums:
            if num in consecutivities:
                continue
            curr = 1
            if num+1 in consecutivities and num-1 in consecutivities:
                right = consecutivities[num+1]
                left = consecutivities[num-1]
                curr = right + left + 1
                consecutivities[num+right] = curr
                consecutivities[num-left] = curr
            elif num+1 in consecutivities:
                curr = consecutivities[num+1] + 1
                consecutivities[num+curr-1] = curr
            elif num-1 in consecutivities:
                curr = consecutivities[num-1] + 1
                consecutivities[num-curr+1] = curr
            consecutivities[num] = curr
            res = max(res, curr)
        return res
