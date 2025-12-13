for _ in range(int(input())):
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(input())

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

    root = TrieNode()
    flag1 = True
    for p in phone:
        node = root
        flag2 = True
        for a in p:
            if a not in node.children:
                node.children[a] = TrieNode()
                flag2 = False
            if node.end:
                flag1 = False
            node = node.children[a]
        node.end = True
        if flag2:
            flag1 = False
    print("YES") if flag1 else print("NO")
