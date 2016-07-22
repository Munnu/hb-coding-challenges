def add_to_zero(listy):
    """ input: list of ints, ret True if any two nums sum to zero """
    # >>> add_to_zero([])
    # False

    # >>> add_to_zero([1])
    # False

    # >>> add_to_zero([1, 2, 3])
    # False

    # >>> add_to_zero([1, 2, 3, -2])
    # True
    if len(listy) == 0:
        return False
    if len(listy) == 1 and listy[0] == 0:
        return True
    for stuff in listy:
        if -stuff in listy:
            return True
    return False
print add_to_zero([])

print add_to_zero([1])

print add_to_zero([1, 2, 3])

print add_to_zero([1, 2, 3, -2])
