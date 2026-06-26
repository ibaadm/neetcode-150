class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        while l < r-1:
            mid = l + (r-l) // 2
            if nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
        return nums[r]