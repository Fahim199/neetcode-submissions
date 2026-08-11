# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        cnt=0
        while queue:
            n = len(queue)
            level = [0]*n
            isZigzag=cnt%2
            currInd = -1
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if isZigzag:
                    level[currInd] = node.val
                    currInd-=1
                else:
                    level[i]= node.val
            result.append(level)
            cnt+=1

        return result

        