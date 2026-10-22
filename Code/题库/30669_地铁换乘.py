from collections import deque,defaultdict
class TreeNode:
    def __init__(self,index):
        self.index=index
        self.child=[]
        self.father=None
        self.depth=0
n,t=map(int,input().split())
dict1=defaultdict(list)
for _ in range(n-1):
    u,v=map(int,input().split())
    dict1[u].append(v)
    dict1[v].append(u)
p,q,v1,v2=map(int,input().split())
root=TreeNode(t)
root.father=TreeNode(-1)
queue=deque([root])
subway=[None,None]
while queue:
    node=queue.popleft()
    a=node.index
    for b in dict1[a]:
        if b!=node.father.index:
            child=TreeNode(b)
            node.child.append(child)
            child.father=node
            child.depth=node.depth+1
            queue.append(child)
            if b==p:
                subway[0]=child
            if b==q:
                subway[1]=child
    if subway[0] and subway[1]:
        break
node1,node2=subway
l1=[]
l2=[]
m=node1.depth-node2.depth
if m>0:
    for _ in range(m):
        l1.append(node1)
        node1=node1.father
else:
    m=-m
    for _ in range(m):
        l2.append(node2)
        node2=node2.father
while True:
    l1.append(node1)
    l2.append(node2)
    if l1[-1]==l2[-1]:
        break
    node1=node1.father
    node2=node2.father
l=l1[:-1]+l2[::-1]
L=len(l)-1
time=int(L/(v1+v2))
depth=l[int(L*v1/(v1+v2))].depth
print(time,depth)