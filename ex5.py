for x in range(99, 0, -1):
    if x > 1:
        print(x, "bottles of beer on the wall,",x,"bottles of beer.")
        if x > 2:
            suff = str(x - 1) + " bottles of beer on the wall."
        else:
            suff = "1 bottle of beer on the wall."
    elif x == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        suff = "no more bottles of beer on the wall."
    print("Take one down, pass it around,", suff)
