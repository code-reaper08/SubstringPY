def substring(Str, n):
    for i in range(0, n):
        for j in range(1, n-i+1):
            substring = ""
            for k in range(1,i+j):
                substring = substring + Str[k]
    print(substring)
Str = "abc"
n = len(Str)
substring(Str,n)
