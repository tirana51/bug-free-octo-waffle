for _ in range(int(input())):
    n=int(input())
    max_speeds = list(map(int, input().split()))
    speed = [max_speeds[0]]
    c=0
    if n==1:
        print(1)
        continue
    for i in range(1, n):
        if speed[i-1]<max_speeds[i]:
            speed.append(speed[i-1])
            c=c+1
        else:
            speed.append(max_speeds[i])
    print(n-c)
