class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while True:
            curr_sum = sorted_nums[i] + sorted_nums[j]
            if curr_sum == target:
                break
            elif curr_sum > target:
                j -= 1
            else:
                i += 1
        if sorted_nums[i] == sorted_nums[j]:
            i = nums.index(sorted_nums[i])
            j = nums.index(sorted_nums[j], i+1)
        else:
            i = nums.index(sorted_nums[i])
            j = nums.index(sorted_nums[j])
        return [min(i, j), max(i, j)]