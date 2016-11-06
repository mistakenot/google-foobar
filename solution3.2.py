import math

def answer(M, F):
    result = get_generation_else_none(long(M), long(F))
    return "impossible" if result == None else str(result)

def get_generation_else_none(m, f):
    """
    Get the generation of this pair if they are valid leaf nodes
    of (1, 1) in the tree.

    :param m: Value representing number of Mach bombs.
    :param f: Value representing number of Facula bombs.
    :return: Generation number or None if invalid.
    
    The model for the tree is:
           (x, y)
           |    |
     (x+y, y)  (x, y+x)

    To go back a generation, we subtract min(x, y) from max(x, y) for one value
    and retain min(x, y) in its same position for the other.
    """
    x = m
    y = f
    gen_count = 0

    if x < 1 or y < 1:
        return None
    
    while x > 1 and y > 1:
        if x % y == 0 or y % x == 0:
            # We would never be able to reach the root node.
            return None

        # Aiming for clarity over DRY
        #
        # Rather than looping over every generation we can optimise
        #  by jumping back multiple generations depending on how large
        #  the difference is between the two numbers.
        elif x > y:
            # n is the number of times we can subtract 
            #  y from x until y > x
            n = math.trunc(x/y)
            x -= (n * y)
            gen_count += n
        else:
            # n is the number of times we can subtract 
            #  x from y until x > y
            n = math.trunc(y/x)
            y -= (n * x)
            gen_count += n
    
    # As soon as either number is 1 we know we are on either
    #  of the extreme edges of the tree. No need to count all the
    #  way back, just add the difference between the two to the 
    #  generation count.
    return gen_count + max(x, y) - min(x, y)

big_str = "100000000000000000000000000000000000000000000000000"
big_int = long(big_str)

print(get_generation_else_none(big_int, 7) == 14285714285714285714285714285714285714285714285718)

print(get_generation_else_none(2, 1) == 1)
print(get_generation_else_none(4, 7) == 4)
print(get_generation_else_none(2, 4) == None)
print(get_generation_else_none(7, 5) == 4)
print(get_generation_else_none(0, 0) == None)
print(get_generation_else_none(1, 0) == None)
print(get_generation_else_none(0, 1) == None)
print(get_generation_else_none(1, 1) == 0)