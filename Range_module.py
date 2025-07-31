import bisect

class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        new = []
        placed = False
        for l, r in self.ranges:
            if r < left or l > right:
                new.append((l, r))
            else:
                left = min(left, l)
                right = max(right, r)
        new.append((left, right))
        new.sort()
        self.ranges = new

    def queryRange(self, left, right):
        for l, r in self.ranges:
            if l <= left and right <= r:
                return True
        return False

    def removeRange(self, left, right):
        new = []
        for l, r in self.ranges:
            if r <= left or l >= right:
                new.append((l, r))
            else:
                if l < left:
                    new.append((l, left))
                if r > right:
                    new.append((right, r))
        self.ranges = new
