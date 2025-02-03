from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Finds the minimum depth of a binary tree using DFS.

        Technique Used:
        - **Recursive DFS Traversal**: Explores both left and right subtrees to find the minimum depth.
        - **Leaf Node Detection**: Returns depth when a leaf node is found.
        - **Handling Skewed Trees**: If one subtree is missing, the function does not return `0` (to avoid counting missing paths as valid).

        Time Complexity: O(N) in the worst case (if the tree is skewed).
        Space Complexity: O(H), where H is the height of the tree (O(log N) for balanced trees, O(N) for skewed trees).
        """
        
        if not root:
            return 0  # Empty tree has depth 0
        
        if not root.left and not root.right:
            return 1  # A single node tree has a depth of 1

        # If a node has only one child, we should not consider the missing child
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist, find the minimum depth
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
# BFS Solution
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Finds the minimum depth of a binary tree using BFS.
        
        Time Complexity: O(N) since we visit each node once.
        Space Complexity: O(N) in the worst case (wide tree with all nodes at the same level).
        """

        if not root:
            return 0

        queue = deque([(root, 1)])  # (node, depth)

        while queue:
            node, depth = queue.popleft()

            # If we reach a leaf node, return its depth
            if not node.left and not node.right:
                return depth

            # Add children to queue if they exist
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))