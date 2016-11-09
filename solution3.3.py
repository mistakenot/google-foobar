import math

def answer(n):
    return 1

qk_cache = {}

def q(k):
    if (qk_cache.has_key(k)):
        return qk_cache[k]

    result_acc = a(k)

    i = 0
    for p in pentagonal_series():
        if p > k:
            qk_cache[k] = result_acc
            return result_acc
        else:
            sign = get_sign(i)
            prev = q(k - p)
            result_acc += (sign * prev)
            i += 1

def a(k):
    """
    a(k) is (-1)^m if k = 3m^2 - m for some integer m, else 0.
    m is calculated using quadratic formula: (-b +|- math.sqrt(b^2 - 4ac)) / 2a
    """
    m1 = (1 + math.sqrt(1 + (12*k))) / 6
    m2 = (1 - math.sqrt(1 + (12*k))) / 6

    if math.trunc(m1) == m1:
        return int(math.pow(-1, m1))
    elif math.trunc(m2) == m2:
        return int(math.pow(-1, m2))
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
    try:
        n = 0
        while True:
            k = math.trunc((n+2)/2) * math.pow(-1, n % 2)
            p = k * ((3 * k) - 1) / 2
            yield p
            n += 1
    except GeneratorExit:
        return

def get_sign(i):
    """
    A function that returns the ith element of the sequence:
    1, 1, -1, -1, 1, 1, -1, -1...
    """
    sign = 1 - ((i % 4) - (i % 2))
    return sign

for i in range(201):
    print(q(i))