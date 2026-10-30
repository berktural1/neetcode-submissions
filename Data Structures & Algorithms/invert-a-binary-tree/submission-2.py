# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # 2 ways to solve this: 
        # breadth-first traversal and reversal
        # depth-first

        # depthfirst makes more sense to me here
        # O(n) time, O(n) extra space b/c of recursive call stack

        # same complexity for breadthfirst solution.

        if root:
            # traverse left side first
            if root.left:
                self.invertTree(root.left)   
            if root.right:
                self.invertTree(root.right)
                
            root.left, root.right = root.right, root.left
        return root

            


        