class TreeNode:
    def __init__(self,s,e):
        self.start=s
        self.end=e
        self.val=0
        self.lazy=0
        self.left=None
        self.right=None
N,Q=map(int,input().split())
def init(s,e):
    if s==e:
        return TreeNode(s,e)
    node=TreeNode(s,e)
    m=(s+e)>>1
    node.left=init(s,m)
    node.right=init(m+1,e)
    return node
root=init(1,N)
for _ in range(Q):
    x=list(input().split())
    if x[0]=='Add':
        l,r,v=map(int,x[1:])
        def add(node,l,r,v):
            s=node.start
            e=node.end
            if s!=e and node.lazy:
                lazy=node.lazy
                node.left.val+=lazy
                node.left.lazy+=lazy
                node.right.val+=lazy
                node.right.lazy+=lazy
                node.lazy=0
            if l<=s and e<=r:
                node.val+=v
                node.lazy+=v
                return
            elif l>e or r<s:
                return
            add(node.left,l,r,v)
            add(node.right,l,r,v)
            node.val=max(node.left.val,node.right.val)
        add(root,l,r,v)
    elif x[0]=='Query':
        l,r=map(int,x[1:])
        def query(node,l,r):
            s=node.start
            e=node.end
            if s!=e and node.lazy:
                lazy=node.lazy
                node.left.val+=lazy
                node.left.lazy+=lazy
                node.right.val+=lazy
                node.right.lazy+=lazy
                node.lazy=0
            if l<=s and e<=r:
                return node.val
            elif l>e or r<s:
                return -float('inf')
            else:
                return max(query(node.left,l,r),query(node.right,l,r))
        print(query(root,l,r))