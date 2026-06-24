import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleet_times = [0]
        for pos, speed in cars:
            time = (target - pos) / speed
            if time > fleet_times[-1]:
                fleet_times.append(time)
        return len(fleet_times) - 1