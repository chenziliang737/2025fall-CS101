class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input())
nodes=[TreeNode(i) for i in range(n)]
condition=[True for _ in range(n)]
for i in range(n):
    l,r=map(int,input().split())
    node=nodes[i]
    if l!=-1:
        node.left=nodes[l]
        condition[l]=False
    if r!=-1:
        node.right=nodes[r]
        condition[r]=False
for i in range(n):
    if condition[i]:
        root=nodes[i]
def dfs1(node,n):
    if node:
        return max(dfs1(node.left,n+1),dfs1(node.right,n+1))
    else:
        return n-1
h=dfs1(root,0)
def dfs2(node):
    if not node.left and not node.right:
        return 1
    elif not node.left:
        return dfs2(node.right)
    elif not node.right:
        return dfs2(node.left)
    else:
        return dfs2(node.left)+dfs2(node.right)
s=dfs2(root)
print(h,s)