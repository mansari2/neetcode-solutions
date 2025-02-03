# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Inserts a new value into a Binary Search Tree (BST) and returns the root node of the modified tree.
        
        Technique Used:
        - **Recursive Tree Traversal**: The function traverses down the tree recursively, 
          ensuring that the BST property (left subtree contains smaller values, right subtree contains larger values) is maintained.
        - **Base Case Handling**: If the tree is empty, a new TreeNode is created and returned.
        - **Recursive Insertion**: The function determines the correct subtree (left or right) to insert the value 
          and recursively calls itself to insert the node.

        Time Complexity: O(log N) in a balanced BST, O(N) in the worst case (unbalanced BST).
        Space Complexity: O(log N) in a balanced BST due to recursive stack calls, O(N) in the worst case.
        """
        
        # Base case: If the tree is empty, create a new node and return it
        if not root:
            return TreeNode(val)
        
        # If the value to insert is greater than the current node's value, insert in the right subtree
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            # If the value is smaller, insert in the left subtree
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the unchanged root node
        return root
