for _ in range(int(input())):
    tot=0
    k,d0,d1=map(int,input().split())
    d2=(d0+d1)%10
    d3=(d2*2)%10
    d4=(d3*2)%10
    d5=(d4*2)%10
    d6=(d5*2)%10
    l=[d3,d4,d5,d6]
    if k==2:
        if (d0+d1)%3==0:
            print("YES")
        else:
            print("NO")
    elif k==3:
        if (d3%3)==0:
            print("YES")
        else:
            print("NO")
    else:
        tot=(d0+d1+d2)+sum(l)*((k-3)//4)
        tot+=sum(l[:(k-3)%4])
        if tot%3==0:
            print("YES")
        else:
            print("NO")
