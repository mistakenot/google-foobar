def​ answer(start,​ ​length):
    result = start
    for group_index in range(length):
        group_start = start + (group_index * length)
        group_length = length - group_index
        result ^= calc_sequence(group_start, group_length)
    
    return result
    
def calc_sequence(start, length):
    result = start
    for i in range(length):
        result ^= (start + i)
    
    return result