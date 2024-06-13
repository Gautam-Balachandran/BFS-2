# Time Complexity : O(n)
# Space Coplexity : O(h)
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        if root is None:
            return []
        self.dfs(root, 0)
        return self.result

    def dfs(self, node: Optional[TreeNode], level: int):
        if node is None:
            return
        if level == len(self.result):
            self.result.append(node.val)
        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)

solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)
print(solution.rightSideView(root1))  # Output: [1, 3, 4]

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.right = TreeNode(5)
print(solution.rightSideView(root2))  # Output: [1, 2, 5]

# Example 3
root3 = TreeNode(1)
root3.right = TreeNode(3)
print(solution.rightSideView(root3))  # Output: [1, 3]