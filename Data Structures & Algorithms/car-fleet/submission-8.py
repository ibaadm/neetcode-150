import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = 0
        last_time = 0
        for pos, speed in cars:
            curr_time = (target - pos) / speed
            if curr_time > last_time:
                fleets += 1
                last_time = curr_time
        return fleets