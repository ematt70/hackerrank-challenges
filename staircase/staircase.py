n=5

for line in range(1,n+1):
    #print("line = " + str(line), end="\n")
    for space in range(n):
    #print("space1 = " + str(space))
        if space < n-line:
            print(" ", end="")
        elif space == n-line:
            for pound in range(space, n):
                #print("space2 = " + str(space))
                #print("pound = " + str(pound))
                if pound in range(n-line, n-1):
                    print("#", end="")
                else:
                    print("#", end="\n")
                pound += 1
        space += 1
    line += 1