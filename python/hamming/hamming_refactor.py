# First attempt - fails 3 tests, isn't clear... but reduce won't work how i want it to...
def distance(strand_a, strand_b):
    la = list(strand_a)
    lb = list(strand_b)
    if len(la) != len(lb):
        raise ValueError("{strand_a}! is not the same length as {strand_b}!")
    else:
        return len([char for char in la if not char in lb or lb.remove(char)])
