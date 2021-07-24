def substring(Str, n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(Str[i: j])

Str = "abc"
n = len(Str)
substring(Str,n)