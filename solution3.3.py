def answer(n):


"""
Problem is finding all unique partitions of number Name
2 can be composed of:
    2
    1 + 1
    (2 combos)

3 can be composed of:
    3
    2 + 1
    1 + 1 + 1
    (3 combos)
4 can be composed of:
    4
    3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
    (5 combos)

5 can be composed of:
    5
    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
    (7 combos)

6 can be composed of:
    6
    5 + 1
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1 
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    (11 combos)

7 can be composed of:
    7
    6 + 1
    5 + 2
    5 + 1 + 1
    4 + 3
    4 + 2 + 1
    4 + 1 + 1 + 1
    3 + 3 + 1
    3 + 2 + 2
    3 + 2 + 1 + 1
    3 + 1 + 1 + 1 + 1
    2 + 2 + 2 + 1
    2 + 2 + 1 + 1 + 1
    2 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1 + 1
    (15 combos)

An algorithm for this would generate the next line by decomposing
whatever number is on the far right of the line until it is all ones.

Once we have all partitions, we can figure out which are unique.
"""

def get_partitions(n):
    res = [n-1, 1]
    
        