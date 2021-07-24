def substring(Str, n):
    for i in range(0, n):
        for j in range(1, j<=n-i):
            substring = ""
            for k in range(1,k<i+j):
                substring = substring + Str[j]
    print(substring)
Str = "abc"
n = len(Str)
