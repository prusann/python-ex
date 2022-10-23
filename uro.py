def wrap(height, width, length):

    MAX = max(height, width, length)
    MIN = min(height, width, length)
    MID = height + width +length - MIN - MAX
    sum = 4* MIN + 2 * (MAX + MID) + 20
    print ('Potrzebujesz ', sum ,'cm wstążki')
    return sum

wrap(1,3,1)