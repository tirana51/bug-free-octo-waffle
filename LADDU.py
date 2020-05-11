for _ in range(int(input())):
    activities, origin = input().split()
    ladoos = 0
    for i in range(int(activities)):
        item = input().split()
        if item[0]=='CONTEST_WON':
            if 20-int(item[1])>0:
                ladoos = ladoos+300+20-int(item[1])
            else:
                ladoos = ladoos+300
        elif item[0]=='TOP_CONTRIBUTOR':
            ladoos = ladoos+300
        elif item[0]=='BUG_FOUND':
            ladoos = ladoos+int(item[1])
        else:
            ladoos = ladoos+50
    if origin=='INDIAN':
        print(int(ladoos/200))
    else:
        print(int(ladoos/400))
