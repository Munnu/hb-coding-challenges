def binary_search(val):
    """ Using binary search, find val in 
        range 1-100. Return # of guesses 
    """
    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    min_val = 0
    max_val = 100

    found = False
    while not found:
        half_val = max_val / 2
        if (max_val/2) < val:
            print "inside of if"
            min_val = max_val/2
        elif (max_val/2) > val:
            max_val = max_val/2 
        else:
            # assume we've reached the guessed number
            found = True
            print "The number is:", half_val

        num_guesses = num_guesses + 1

    return "The number of guesses: %d" % (num_guesses)

print binary_search(25)
