# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # check if you are at a root, if yes calculate max depth of its
        # subtrees if you are at an empty node, return 0.

        # O(n) time and extra space complexity

        # cleaned up logic a bit
        # deal with base case first
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        


        
        


        