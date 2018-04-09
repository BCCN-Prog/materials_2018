def find_maxima(x,circular=False):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers
        circular - Bool, if True first and last are considered neighbours
    Output:
        idx -- list of indices of the local maxima in x
    """

    if not circular:
        idx = []

        if x[0]>x[1]:
            idx.append(0)

        for i in range(1,len(x)-1):
            # `i` is a local maximum if the signal decreases before and after it
            if x[i-1] < x[i] and x[i+1] < x[i]:
                idx.append(i)

        if x[-1]>x[-2]:
            idx.append(len(x))

    if circular: idx = [i for i in range(len(x)) if x[i-1] < x[i] and x[(i+1)%len(x)] < x[i]]

    return idx
