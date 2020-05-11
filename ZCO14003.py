n=int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
j = n-1 
max1 = l[0]*n
for i in range(1,n):
    if l[i]*j > max1:
        max1 = l[i]*j 
    j = j - 1
print(max1)
