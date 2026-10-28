# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # invert = switch left/right for each node
        # initial thought: depthfirst traversal of the tree with recursion and
        # switching pointers

        # original: while root.left or root.right
        if root: # check that the node you are on has children

            self.invertTree(root.left)
            self.invertTree(root.right)
            # after exploring both children paths to where they don't have children
            # switch pointers
            root.left, root.right = root.right, root.left
        

        return root
        