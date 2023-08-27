for i in range(int(input())):
    n=int(input())
    s=input()
    c=0
    f=False
    vowels=['a','e','i','o','u']
    for j in s:
        if j not in vowels:
            c+=1
        else:
            c=0
        if c>=4:
            f=True
    if f:
        print("NO")
    else:
        print("YES")
