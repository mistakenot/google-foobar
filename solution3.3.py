import math

def answer(n):
    return 1

def q(k):
    # Accumulate the result
    result = a(k)
    # Number of loop iterations
    i = 0
    # Used to control +|- flipping in sequence
    flip = 1
    while k >= pentagonal(i):
        # Generates 0, 1, 1, 0, 0, 1, 1, 0, 0...
        flip = (flip + (k % 2)) % 2
        sign = math.pow(-1, flip)
        pent = pentagonal(i)
        prev = q(k - pent)

        log = (k, sign, pent)
        print(log)
        result += (math.pow(-1, flip) * prev)
        i += 1

    return result

def a(k):
    """
    a(k) is (-1)^m if k = 3m^2 - m for some integer m, else 0.
    m is calculated using quadratic formula: (-b +|- math.sqrt(b^2 - 4ac)) / 2a
    """
    m1 = (1 + math.sqrt(1 + (12*k))) / 6
    m2 = (1 - math.sqrt(1 + (12*k))) / 6

    if math.trunc(m1) == m1:
        return math.pow(-1, m1)
    elif math.trunc(m2) == m2:
        return math.pow(-1, m2)
    else:
        return 0

def pentagonal(n):
    """
    Iterator of the values of the pentagonal series.
    Equal to k(3k-1)/2 for k = 1, −1, 2, −2, 3
    e.g. 1, 2, 5, 7, 12...
    """
    k = math.trunc((n+2)/2) * math.pow(-1, n % 2)
    p = k * ((3 * k) - 1) / 2
    return p

def pentagonal_series():
    i = 0
    while True:
        yield pentagonal(i)
        i += 1

print("k", "sign", "pent")
for k in pentagonal_series():
    print(k)