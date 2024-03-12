import time
import gen

class Results():
    def __init__(self) -> None:
        self.runs = []
    def add(self, time: float):
        self.runs.append((time))
    def min(self)->float:
        return min(self.runs)
    def max(self)->float:
        return max(self.runs)
    def avg(self)->float:
        return sum(self.runs)/len(self.runs)

def run(arrfn, sortfn, arrlen, times) -> Results:
    res = Results()
    for i in range(times):
        arr = arrfn(arrlen)
        start = time.perf_counter()
        sortfn(arr)
        end = time.perf_counter()
        res.add(end-start)
    return res

def plot(res: dict[str, Results]):
    pass

def test(name ,sortfn, arrlen):
    print(name)
    res: dict[str, Results] = {}
    for arrfn in [gen.Rand, gen.Asc, gen.Desc, gen.A, gen.V]:
        res[arrfn.__name__] = run(arrfn, sortfn, arrlen, 10)
    for key, val in res.items():
        print(f"\t{key}:\tmin:{val.min():8f}\tmax:{val.max():8f}\tavg:{val.avg():8f}")
    plot(res)

def debug(arrfn, sortfn, arrlen):
    arr = arrfn(arrlen)
    print(f"In: {arr}")
    sortfn(arr)
    print(f"Out: {arr}")
