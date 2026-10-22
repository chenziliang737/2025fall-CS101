class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
from collections import deque
n=int(input())
preorder=list(map(int,input().split()))
inorder=sorted(preorder)
sumtree=inorder[:]
for i in range(n-2,-1,-1):
    sumtree[i]+=sumtree[i+1]
def dfs(l1,r1,l2,r2):
    if l1>r1:
        return None
    val=preorder[l1]
    idx=inorder.index(val)
    left_length=idx-l2
    right_length=r2-idx
    node=TreeNode(sumtree[idx])
    node.left=dfs(l1+1,l1+left_length,l2,idx-1)
    node.right=dfs(r1-right_length+1,r1,idx+1,r2)
    return node
root=dfs(0,n-1,0,n-1)
queue=deque([root])
res=[]
while queue:
    node=queue.popleft()
    res.append(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
print(*res)