c=1
while True:
    p,e,i,d=map(int,input().split())
    if (p,e,i,d)==(-1,-1,-1,-1):
        break
    s=0
    for day in range(p%23,30000,23):
        if (day-e)%28==0 and (day-i)%33==0:
            if day>d:
                s=day-d
            else:
                s=day+21252-d
            break
    print(f'Case {c}: the next triple peak occurs in {s} days.')
    c+=1