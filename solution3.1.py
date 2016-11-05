def answer(start, length):
    result = 0
    for row in range(length):
        i = (row * length) + start 
        result ^= xor_sum(i, i + length) ^ xor_sum(i + length - row,  i + length)

    return result

def xor_sum(a, b):
    """
    XOR sum of sequence of positive ints starting at a and finishing at b.
    
    Equivilent to fold using (_ ^ _) over range(a, b).
    """
    if a < 0 | b < 0:
        return None

    if a == 0:
        if b % 2 == 0: return 0
        else: return b - 1
    else:
        return xor_sum(0, a) ^ xor_sum(0, b)