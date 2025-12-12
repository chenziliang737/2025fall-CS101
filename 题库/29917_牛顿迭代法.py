from decimal import Decimal
while True:
    try:
        d=Decimal(input())
    except EOFError:
        break
    x=Decimal('inf')
    y=Decimal('1')
    n=0
    while abs(y-x)>1E-6:
        x=y
        y=x-(x**2-d)/(2*x)
        n+=1
    print(f'{n} {y:.2f}')