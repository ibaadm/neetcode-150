class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = []
        for num in nums_set:
            if num - 1 not in nums_set:
                starts.append(num)
        res = 0
        for start in starts:
            curr_streak = 1
            curr_num = start
            while curr_num + 1 in nums_set:
                curr_streak += 1
                curr_num += 1
            res = max(res, curr_streak)
        return res