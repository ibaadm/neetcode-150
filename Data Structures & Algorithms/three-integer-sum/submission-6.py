class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i, x in enumerate(nums):
            if x > 0:
                break
            
            if i and x == nums[i-1]:
                continue

            l = i+1
            r = n-1
            while l < r:
                y = nums[l]
                z = nums[r]
                if y + z == -x:
                    res.append([x, y, z])
                    while l < r and nums[l] == y:
                        l += 1
                    r -= 1
                elif y + z < -x:
                    l += 1
                else:
                    r -= 1
        return res