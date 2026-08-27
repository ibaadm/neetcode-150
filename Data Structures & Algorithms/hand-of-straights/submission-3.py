class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = [0] * 1001

        for val in hand:
            count[val] += 1



        for i in range(1001):
            if curr := count[i]:
                if i > 1001 - groupSize:
                    return False
                for j in range(1, groupSize):
                    count[i + j] -= curr
                    if count[i + j] < 0:
                        return False

        return True
