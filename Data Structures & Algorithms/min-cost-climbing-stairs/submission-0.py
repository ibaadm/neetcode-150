class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last_step = 0
        second_last_step = 0
        for i in range(2, len(cost)+1):
            last_step, second_last_step = min(last_step + cost[i-1], second_last_step + cost[i-2]), last_step
        return last_step