def substring (Str,n):
    for i in range(n):
        print(i) #0 #1
        for j in range(i ,n):  #0 to 3  #1 to 3
            for k in range(i, (j + 1)):  #0 to 1 => 0  #1 to 2 => 1
                print(Str[k], end="")  #print 0th element of the string.  #print 0th and 1st element side by side.
            print()

Str = "abc"
n = len(Str)
substring(Str,n)
