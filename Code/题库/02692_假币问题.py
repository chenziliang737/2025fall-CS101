n=int(input())
for _ in range(n):
    def check(coin,weigh,str1,str2):
        if coin in str1:
            if weigh=='heavy':
                return 'up'
            else:
                return 'down'
        elif coin in str2:
            if weigh=='heavy':
                return 'down'
            else:
                return 'up'
        else:
            return 'even'
    list1=[]
    for i in range(3):
        list1.append(input())
    for coin in 'ABCDEFGHIJKL':
        for weigh in ['heavy','light']:
            T=True
            for i in range(3):
                str1,str2,out=list1[i].split()
                if out!=check(coin,weigh,str1,str2):
                    T=False
                    break
            if T:
                print(f'{coin} is the counterfeit coin and it is {weigh}.')
                break