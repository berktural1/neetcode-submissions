# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # rewrite after seeing solution

        # key here: it is 2 problems, not one
        # naive: just the height of the left + height of right
        # need to also keep track of max diameter, which differs

        # O(n) time and extra space

        
        # class variable to keep track of max diameter encountered
        self.diam = 0
        # helper function for dfs

        def dfs(root):

            # handle encountering a leaf node
            if not root:
                return 0

            # find the height of the left and right nodes
            left = dfs(root.left)
            right = dfs(root.right)

            self.diam = max(self.diam, left+right)
            return 1 + max(left, right)
        
        dfs(root) # actual call to recursive function
        return self.diam

            

        