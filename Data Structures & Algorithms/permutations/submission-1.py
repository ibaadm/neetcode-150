class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _permute(i):
            if i == len(nums) - 1:
                return [[nums[i]]]

            others = _permute(i+1)
            num = nums[i]
            curr = []
            for j in range(len(others[0])+1):
                for other in others:
                    curr.append(other[:j] + [num] + other[j:])
            return curr

        return _permute(0)
