import bisect

class ExamRoom:
    def __init__(self, N):
        self.N = N
        self.seats = []

    def seat(self):
        if not self.seats:
            self.seats.append(0)
            return 0
        dist, seat = self.seats[0], 0
        for a, b in zip(self.seats, self.seats[1:]):
            d = (b - a) // 2
            if d > dist:
                dist, seat = d, a + d
        if self.N - 1 - self.seats[-1] > dist:
            seat = self.N - 1
        bisect.insort(self.seats, seat)
        return seat

    def leave(self, p):
        self.seats.remove(p)
