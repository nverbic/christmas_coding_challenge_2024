"""
Challenge 104. 
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Running in main():
Max depth of the binary tree [3, 9, 20, None, None, 15, 7] is 3
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        start = deque()
        start.append(root)
        depth = 0

        while start:
            depth += 1
            for _ in range(len(start)):
                node = start.popleft()
                if node.left:
                    start.append(node.left)
                if node.right:
                    start.append(node.right)
        return depth

if __name__ == "__main__":
    bin_tree_array = [3,9,20,None,None,15,7]
    
    root = TreeNode(bin_tree_array[0])

    q = [root]
    i = 1
    while i < len(bin_tree_array):
        curr = q.pop(0)
        if i < len(bin_tree_array):
            curr.left = TreeNode(bin_tree_array[i])
            q.append(curr.left)
            i += 1
        if i < len(bin_tree_array):
            curr.right = TreeNode(bin_tree_array[i])
            q.append(curr.right)
            i += 1
    
    s = Solution()
    res = s.maxDepth(root)
    print(f" Max depth of the binary tree {bin_tree_array} is {res}")