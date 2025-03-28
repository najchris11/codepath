class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(11, TreeNode(5), TreeNode(6))
badRoot = TreeNode(10, TreeNode(5), TreeNode(6))

# print(root)

# def checkTree(root):
#     return root.val == root.left.val + root.right.val
# print(checkTree(root))

# def check_tree(root):
#     if root.left and root.right:
#         return root.val == root.left.val + root.right.val
#     elif root.left:
#         return root.val == root.left.val
#     elif root.right:
#         return root.val == root.right.val
#     elif root:
#         return True
#     else: 
#         return False
    
# print(check_tree(root))
# print(check_tree(badRoot))

# def left_most(root):
#     curr = root
#     while curr.left:
#         curr = curr.left
#     return curr.val

# print(left_most(root))
# print(left_most(TreeNode(10)))

# def left_most(root):
#     if not root.left:
#         return root.val
#     else: return left_most(root.left)

# print(left_most(root))
# print(left_most(TreeNode(10)))
# def inorder_traversal(root):
#     if not root:
#         return []
#     else:
#         return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
    
# print (inorder_traversal(root))
# coolTree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
# print(inorder_traversal(coolTree))    

# def size(root):
#     if not root:
#         return 0
#     else:
#         return size(root.left) + 1 + size(root.right)
    
# print(size(coolTree))

# def find(root, value):
#     if root and root.val == value:
#         return True
#     elif root:
#         return find(root.left, value) or find(root.right, value)
#     else:
#         return False
    
# print(find(coolTree, 2))

def descending_leaves(root):
    