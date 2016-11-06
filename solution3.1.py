def answer(start, length):
    result = 0
    for row in range(length):
        row_start = (row * length) + start
        row_end = row_start + length
        result ^= xor_sum(row_start, row_end) ^ xor_sum(row_end - row,  row_end)

    return result

def xor_sum(a, b):
    """
    XOR sum of sequence of positive ints between a and b inclusive.
    
    Equivilent to fold using (_ ^ _) over range a -> b.

    :param a: Start of sequence. Must be >= 0.
    :param b: End of sequence. Must be >= 0.
    :return: returns XOR sum as int.
    """
    if a < 0 | b < 0:
        raise Exception("Parameters must be positive.")
    if b < a:
        return xor_sum(b, a)

    if a == 0:
        if b % 4 == 0: 
            return b
        elif b % 4 == 1:
            return 1
        elif b % 4 == 2:
            return b + 1
        else: 
            return 0
    else:
        return xor_sum(0, a - 1) ^ xor_sum(0, b)