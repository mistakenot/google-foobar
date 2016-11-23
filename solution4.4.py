import itertools

def answer(num_buns, num_required):
    # Brute force approach. Start with most basic keyset ([0]) and test
    #  whether conditions hole:
    #  1) Any k subset is union equal to keyset K 
    #  2) Any k-1 subset is not union equal to keyset K
    # 
    # If conditions are not met, increase the number of keys given to each
    #  minion and repeat. If you cannot create N unique keysets, add a new 
    #  key value to the possible keys.

    # N is the number of keys held by each bunny 
    N = 1

    # K is the number of keys to choose from, 0 delimited
    all_keys = set(range(0))

    # The current set of keys being investigated
    distribution = [[0] for x in range(num_buns)]

    # Short circuit conditions 
    if num_required > num_buns:
        raise Exception("Not enough bunnies to open.")
    if num_required == num_buns:
        distribution = [[x] for x in range(num_buns)]
        all_keys = set([x for x in range(num_buns)])

    #while not (is_valid(all_keys, distribution, num_required) and not is_valid(all_keys, distribution, num_required - 1):
     #   t = 1
    
    return distribution

def is_valid_solution(all_keys, solution, num_bunnies):
    return (
        any_r_subsets_cover_universe(all_keys, solution, num_bunnies) and
        not any_r_subsets_cover_universe(all_keys, solution, num_bunnies - 1))

def any_r_subsets_cover_universe(universe_set, current_set, r):
    if r == 0: return False
    if len(universe_set) == 0: return True
    if len(current_set) == 0: return False

    # 1) Generate all combinations of current_set with r elements
    # 2) Compare union of each against universe_set
    # 3) False if any dont match, else true
    all_combinations_of_subsets = itertools.combinations(current_set, r)
    
    for sets in all_combinations_of_subsets:
        union_of_subsets = reduce(lambda x, y: x.union(y), sets)
        if union_of_subsets != universe_set:
            return False

    return True

universe = set(range(3))
test_set = [set([0, 1]), set([1, 2]), set([0, 2])]
print(is_valid_solution(universe, test_set, 2) == True)

universe = set(range(10))
test_set = [
    set([0, 1, 2, 3, 4, 5]),
    set([0, 1, 2, 6, 7, 8]),
    set([0, 3, 4, 6, 7, 9]),
    set([1, 3, 5, 6, 8, 9]),
    set([2, 4, 5, 7, 8, 9])
]
print(is_valid_solution(universe, test_set, 3) == True)

universe = set(range(4))
test_set = [
    set([0]),
    set([1]), 
    set([2]), 
    set([3])
]
print(is_valid_solution(universe, test_set, 4) == True)

universe = set(range(1))
test_set = [
    set([0]),
    set([0])
]
print(is_valid_solution(universe, test_set, 0) == False)
