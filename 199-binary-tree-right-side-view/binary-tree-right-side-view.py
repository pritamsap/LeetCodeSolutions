# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        
        if root: q.append(root)
        res = []
        depth = 0
        while q:
            currLen = len(res)
            for i in range(len(q)):
                node = q.popleft()
                
                if len(res) < currLen + 1:
                    if node: res.append(node.val)            

                if node:
                    q.append(node.right)
                    q.append(node.left)

        return res
            

        