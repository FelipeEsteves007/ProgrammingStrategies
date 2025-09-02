import math

MICRO_S = 1_000_000
MICRO_MIN = 60_000_000

def f_nlogn(n):
    return 0 if n <= 1 else n * math.log2(n)

def f_n2(n):  return n * n
def f_n3(n):  return n ** 3
def f_2n(n):  return 2 ** n
def f_fact(n): return math.factorial(n)

def max_n_for_time(func, t_micro):
    n = 0
    while True:
        if func(n+1) > t_micro:
            return n
        n += 1

cases = [
    ("n log n", f_nlogn),
    ("n^2",      f_n2),
    ("n^3",      f_n3),
    ("2^n",      f_2n),
    ("n!",       f_fact),
]

for name, func in cases:
    n1 = max_n_for_time(func, MICRO_S)
    n2 = max_n_for_time(func, MICRO_MIN)
    print(f"{name}: 1s = {n1}")
    print(f"{name}: 1min = {n2}")
