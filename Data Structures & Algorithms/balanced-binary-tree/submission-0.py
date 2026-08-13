# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        isBalanced = 1

        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right)>1:
                isBalanced*=0
            else: isBalanced*=1

            return 1+ max(left,right)
        
        dfs(root)

        return isBalanced>0
        

        