class Solution:
    def climbStairs(self, n: int) -> int:
        last_two = [1, 1]
        for i in range(1, n):
            last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
        return last_two[1]