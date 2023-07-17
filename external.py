class none:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return

    visited = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        visited.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return visited

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(bfs(root)) # Output: [1, 2, 3, 4, 5, 6, 7]
