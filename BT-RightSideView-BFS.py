# Time Complexity : O(n), where n is the number of nodes
# Space Coplexity : O(h)m where h is the height of the tree
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

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