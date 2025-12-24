# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return the kth smallest value
        # heap approach
        heap = []

        def dfs(node):
            if node:
                heapq.heappush(heap, node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        i = 1
        while i < k:
            heapq.heappop(heap)
            i +=1
        
        smallestVal = heapq.heappop(heap)
        return smallestVal



                


        