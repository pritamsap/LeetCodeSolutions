# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # determine if a binary serach tree is valid or not 
        # all values on left have to greater than node, all values on right great
        stack = []
        stack.append((root, float('-inf'), float('inf') ))

        while stack:
            node, left, right = stack.pop()
            if node.val > left and node.val < right:             
                # append left value:
                if node.left:
                    stack.append((node.left, left, node.val))
                if node.right:
                    stack.append((node.right, node.val, right))
            else:
                return False
        return True

        
            
                

        