def f(x):
    return x**3-5*x**2+10*x-80
l=5
r=6
while r-l>10**(-11):
    m=(l+r)/2
    a=f(m)
    if a<=0:
        l=m
    else:
        r=m
print(f'{m:.9f}')