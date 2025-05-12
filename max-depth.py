
from collections import deque

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def maxDepth(root):
    tree = buildTree(root)
    max = getMaxDepth(tree)
    return max

def getMaxDepth(root):
    
    if not root:
        return 0
    
    left = getMaxDepth(root.left)
    right = getMaxDepth(root.right)
    
    return max(left, right) + 1

def buildTree(values):
    
    if not values or values[0] is None:
        return None
    
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = Node(values[i])
            queue.append(current.left)
        i+= 1
        
        if i < len(values) and values[i] is not None:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1
        
    return root
            
    
print(maxDepth([3, 9, 20, None, None, 15, 7])) # 3
print(maxDepth([1, None, 2])) # 2