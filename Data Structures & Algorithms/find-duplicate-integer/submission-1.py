class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[j] == num:
                    return num
                