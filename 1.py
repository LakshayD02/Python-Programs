class Node:
    def__init_(self,val):
    self.val = val
    self.left = left
    self.right = None
        
    def bfs(root):
        if rootisnone:
            return
        visited []
        queue = [root]
        whilequeue:
            
        node = queue.pop(0)
        visited.append(node.val)
        
    ifnode.left:
    queue.append(node.left)
    ifnode.right:
    queue.append(node.right)
            
    returnvisited

# example binary tree
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(bfs(root)) # Output: [1, 2, 3, 4, 5, 6, 7]

        
        
#     def__init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# defbfs(root):
#     ifrootisNone:
#         return

#     visited = []
#     queue = [root]
    
#     whilequeue:
#         node = queue.pop(0)
#         visited.append(node.val)
        
#         ifnode.left:
#             queue.append(node.left)
#         ifnode.right:
#             queue.append(node.right)
            
#     returnvisited

# # example binary tree
# #       1
# #     /   \
# #    2     3
# #   / \   / \
# #  4   5 6   7
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# print(bfs(root)) # Output: [1, 2, 3, 4, 5, 6, 7]
