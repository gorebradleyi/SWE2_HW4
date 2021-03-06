def listAve(l):
    assert(len(l) > 0), "Average of Empty Set is Undefined"
    total = 0
    for x in l:
        assert(isinstance(x, int) or isinstance(x, float)), "List Must Only Contain Ints and Floats"
        total += x

    return total / len(l)