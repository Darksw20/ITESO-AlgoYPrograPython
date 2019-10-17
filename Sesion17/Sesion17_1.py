for x in range(0,7,1):
    for y in range(0,7,1):
        if y >= x:
            print(f""+str(x)+"-"+str(y)+" ",end="")
    print("")
