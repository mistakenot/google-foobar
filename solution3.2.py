def answer(M, F):
    # Start with 1M, 1F
    # M is on the right
    # F is on the left
    return (1, 1)


# Model as a tree:
#           (x, y)
#           /     \
#     (x+y, y)      (x, y+x)
#     /    \         /    \
# (x+2y, y)(x+y, x+y)

def get_tree(start, n):
    if n == 0:
        return [start, [], []]
    else:
        left, right  = get_next_generation(start)
        return [start, [get_tree(left, n-1), get_tree(right, n-1)]]

def get_next_generation(pair_of_vectors):
    m = pair_of_vectors[0]
    f = pair_of_vectors[1]
    # Left: (m+f, f)
    left = (add_v(m, f), f)
    # Right: (m, f+m)
    right = (m, add_v(m, f))
    return (left, right)

def add_v(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def total_v(v):
    return v[0] + v[1]

start = ((1,0), (0,1))
next = get_next_generation(start)
tree = get_tree(start, 3)
print(tree)