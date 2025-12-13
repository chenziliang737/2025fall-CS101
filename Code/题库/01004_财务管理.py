from decimal import Decimal

list1 = []
for _ in range(12):
    list1.append(Decimal(input()))
m = sum(list1) / 12
print(f'${m:.2f}')
