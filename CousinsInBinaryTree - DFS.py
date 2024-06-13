# Time Complexity : O(n)
# Space Coplexity : O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.xLvl = -1
        self.yLvl = -1
        self.xParent = None
        self.yParent = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None or root.val == x or root.val == y:
            return False
        self.dfs(root, None, 0, x, y)
        return (self.xLvl == self.yLvl) and (self.xParent != self.yParent)

    def dfs(self, node: Optional[TreeNode], parent: Optional[TreeNode], depth: int, x: int, y: int):
        if node is None or (self.xLvl != -1 and self.yLvl != -1):
            return
        self.dfs(node.left, node, depth + 1, x, y)
        if node.val == x:
            self.xParent = parent
            self.xLvl = depth
        elif node.val == y:
            self.yParent = parent
            self.yLvl = depth
        self.dfs(node.right, node, depth + 1, x, y)

# Examples
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
print(solution.isCousins(root1, 4, 3))  # Output: False

# Example 2
solution = Solution()
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(5)
print(solution.isCousins(root2, 4, 5))  # Output: True

# Example 3
solution = Solution()
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.right = TreeNode(4)
root3.right.left = TreeNode(5)
print(solution.isCousins(root3, 4, 5))  # Output: True