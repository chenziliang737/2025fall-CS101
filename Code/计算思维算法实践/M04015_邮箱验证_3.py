import re

while True:
    try:
        email = input().strip()
        if not email:
            break
        if (
            (email.count("@") == 1)
            and (not re.search("^\.|^@|\.$|@$|@\.|\.@", email))
            and ("." in email.split("@")[1])
        ):
            print("YES")
        else:
            print("NO")
    except:
        break
