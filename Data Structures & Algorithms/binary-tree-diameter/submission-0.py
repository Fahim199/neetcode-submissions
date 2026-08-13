# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0 

        def calcHeight(root):
            nonlocal diameter
            
            #baseCase
            if not root:
                return 0
            
            leftSubtree = calcHeight(root.left)
            rightSubtree = calcHeight(root.right)

            diameter = max(diameter, leftSubtree+rightSubtree)
            
            #height Calculation
            return 1 + max(leftSubtree, rightSubtree)
        
        calcHeight(root)
        return diameter
        