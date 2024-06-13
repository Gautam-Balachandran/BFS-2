# Time Complexity : O(n)
# Space Coplexity : O(n)
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None or root.val == x or root.val == y:
            return False
        
        queue = deque([root])
        while queue:
            size = len(queue)
            x_found = y_found = False
            for _ in range(size):
                node = queue.popleft()
                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False
        return False

solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
print(solution.isCousins(root1, 4, 3))  # Output: False

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(5)
print(solution.isCousins(root2, 4, 5))  # Output: True

# Example 3
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.right = TreeNode(4)
root3.right.left = TreeNode(5)
print(solution.isCousins(root3, 4, 5))  # Output: True