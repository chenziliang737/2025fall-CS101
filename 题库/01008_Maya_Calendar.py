import re


def calendar(day, month, year):
    dict1 = {'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5, 'yoxkin': 6, 'mol': 7, 'chen': 8, 'yax': 9,
             'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13, 'muan': 14, 'pax': 15, 'koyab': 16, 'cumhu': 17,
             'uayet': 18}
    dict2 = {0: 'imix', 1: 'ik', 2: 'akbal', 3: 'kan', 4: 'chicchan', 5: 'cimi', 6: 'manik', 7: 'lamat', 8: 'muluk',
             9: 'ok', 10: 'chuen', 11: 'eb', 12: 'ben', 13: 'ix', 14: 'mem', 15: 'cib', 16: 'caban', 17: 'eznab',
             18: 'canac', 19: 'ahau'}
    date = day + 20 * dict1[month] + 365 * year
    day_1 = date % 13 + 1
    month_1 = dict2[date % 20]
    year_1 = date // 260
    return day_1, month_1, year_1


n = int(input())
print(n)
for _ in range(n):
    str1 = input()
    day = int(re.search(r'^\d+', str1).group())
    month = re.search(r'\b[a-z]+\b', str1).group()
    year = int(re.search(r'\d+$', str1).group())
    day_1, month_1, year_1 = calendar(day, month, year)
    print(f'{day_1} {month_1} {year_1}')
