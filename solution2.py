def answer(l):
    return sorted(l, compare)
    
def compare(item1, item2):
    """Version string comparator.

    Implementation of a custom comparator function that 
    will parse each string into a (major, minor, revision) tuple
    before comparing each section in turn.
    
    """
    version_num1 = parse_tuple(item1)
    version_num2 = parse_tuple(item2)

    majors = cmp(version_num1[0], version_num2[0])
    if majors != 0:
        return majors

    minors = cmp(version_num1[1], version_num2[1])
    if minors != 0:
        return minors

    return cmp(version_num1[2], version_num2[2])

def parse_tuple(str_version_number):
    """Parse a version string into a tuple of (Major, Minor, Revision)"""
    version_sections = str_version_number.split('.')
    int_version_sections = map(int, version_sections)
    major = get_or_none(int_version_sections, 0)
    minor = get_or_none(int_version_sections, 1)
    rev = get_or_none(int_version_sections, 2)

    return (major, minor, rev)

def get_or_none(items, i):
    if i < len(items): return items[i]
    else: return None

result = answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print(result)