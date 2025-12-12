class TrieNode:
    def __init__(self):
        self.chd = {}
        self.is_end = 0
        self.dp = 0
def build_trie(words):
    root = TrieNode()
    for w in words:
        node = root
        for s in w:
            if s not in node.chd:
                node.chd[s] = TrieNode()
            node = node.chd[s]
        node.is_end = 1
    return root
def dfs(u):
    product = 1
    for v in u.chd.values():
        dfs(v)
        product *= v.dp
    u.dp = product + u.is_end
n = int(input())
words = [input() for _ in range(n)]
root = build_trie(words)
dfs(root)
print(root.dp)