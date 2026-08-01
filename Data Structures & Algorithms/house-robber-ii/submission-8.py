class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def linearly_rob(l, r):
            rob1 = 0
            rob2 = 0
            for i in range(l, r):
                num = nums[i]
                rob1, rob2 = max(rob1, rob2 + num), rob1
            return rob1

        return max(linearly_rob(0, len(nums)-1), linearly_rob(1, len(nums)))