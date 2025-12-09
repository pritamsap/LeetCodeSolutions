# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack = []
        stack.append((root, float('-inf'), float('inf')))

        while stack:
            node, lower, upper = stack.pop()

            if node and node.val > lower and node.val < upper:
                if node.left: stack.append((node.left, lower, node.val))
                if node.right: stack.append((node.right, node.val, upper))
            else:
                return False       

        return True
            
                

        