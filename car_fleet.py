class Solution:
    def carFleet(self, target, position, speed):
        pairs = sorted(zip(position, speed), reverse=True)
        fleets, cur_time = 0, 0
        for p, s in pairs:
            t = (target - p) / s
            if t > cur_time:
                fleets += 1
                cur_time = t
        return fleets
