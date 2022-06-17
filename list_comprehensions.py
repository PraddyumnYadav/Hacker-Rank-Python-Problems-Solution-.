if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Creat List for all coordinates
    x = [p for p in range(x+1)]
    y = [q for q in range(y+1)]
    z = [r for r in range(z+1)]
    
    # list of all coordinates
    perm = [[i, j, k] for i in x for j in y for k in z]

    # list of coordinates that are not equal to 3
    reqList = [l for l in perm if sum(l) != n]
    print(reqList)
