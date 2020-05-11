for _ in range(int(input())):
    for game in range(int(input())):
        i, n, q = list(map(int, input().split()))
        h, t=0, 0
        if n%2==0:
            print(n//2)
        else:
            if i==1:
                t=n//2+1
                h=n//2
            else:
                t=n//2
                h=n//2+1
            if q==1:
                print(h)
            else:
                print(t)
