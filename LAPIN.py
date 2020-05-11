for _ in range(int(input())):
    s = input()
    l = len(s)
    c=0
    if l%2==0:
        s1 = s[:l//2]
        s2 = s[l//2:]
    else:
        s1 = s[:l//2]
        s2 = s[l//2+1:]
    set1 = set(s1)
    set2 = set(s2)
    if set1!=set2:
        c=1
    else:
        for e in set1:
            if s1.count(e)!=s2.count(e):
                c=c+1
                break
    if c==0:
        print('YES')
    else:
        print('NO')
