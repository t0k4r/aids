import statistics

class Results:
    def __init__(self) -> None:
        self.values: list[float] = []
    def min(self):
        return min(self.values)
    def max(self):
        return max(self.values)
    def avg(self):
        return sum(self.values)/len(self.values)
    def stdev(self):
        return statistics.stdev(self.values)
        pass

# import time
# def run(fn) -> Results:
#     r = Results()
#     for _ in range(10):
#         start = time.time()
#         fn()
#         r.values.append(time.time()-start)
#     return r


# def runrange(fn, lo, hi)->list[Results]:
#     r = []
#     while lo <= hi:
#         lo*=10
#         r.append(run(fn))
#     return r
    