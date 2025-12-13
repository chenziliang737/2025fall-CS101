word = " " + input().lower() + " "
s = " " + input().lower() + " "
list1 = list(s.split())
a = s.find(word)
if a == -1:
    print(-1)
else:
    b = list1.count(word.strip())
    print(f"{b} {a}")
