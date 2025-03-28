class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# minDiff = float("inf")
# def min_diff_in_bst(root):
#     global minDiff
#     if not root:
#         return minDiff
#     else:
#         if root.right:
#             if abs(root.right.val - root.val) < minDiff: minDiff = abs(root.right.val - root.val)
#         if root.left:
#             if abs(root.left.val - root.val) < minDiff: minDiff = abs(root.left.val - root.val)
#         return min(min_diff_in_bst(root.right), min_diff_in_bst(root.left))

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# print(min_diff_in_bst(root))

# def increasing_bst(root):
#     def inorder_traversal(root):
#         if not root:
#             return []
#         else:
#             return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
#     lst = inorder_traversal(root)
#     retVal = TreeNode(lst[0])
#     curr = retVal
#     for i in range(1, len(lst)):
#         curr.right = TreeNode(lst[i])
#         curr = curr.right
#     return retVal
# print(increasing_bst(root).right.right.val)

def can_split(root):
    def size(root):
        if not root:
            return 0
        else:
            return size(root.left) + 1 + size(root.right)
    if (abs(size(root.left)-size(root.right)) > 1):
        return False
    return True
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
# root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(can_split(root1))
