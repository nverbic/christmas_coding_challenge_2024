"""
Challenge 100. 

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

TODO: Test recursive solution
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

Running in main():
Binary trees: [3, 9, 20] and [3, 9, 20] are the same:  True
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        start_1 = deque()
        start_1.append(p)
        start_2 = deque()
        start_2.append(q)

        while start_1 and start_2:
            for _ in range(len(start_1)):
                node_1 = start_1.popleft()
                node_2 = start_2.popleft()
                if node_1.val != node_2.val:
                    return False
                if node_1.left and node_2.left:
                    start_1.append(node_1.left)
                    start_2.append(node_2.left)
                elif node_1.left or node_2.left:
                    return False
                if node_1.right and node_2.right:
                    start_1.append(node_1.right)
                    start_2.append(node_2.right)
                elif node_1.right or node_2.right:
                    return False

        return True

def create_tree(bin_tree_array: list) -> TreeNode:
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
    return root

if __name__ == "__main__":
    bin_tree_array_1 = [3,9,20]
    bin_tree_array_2 = [3,9,20]
    root_1 = create_tree(bin_tree_array_1)
    root_2 = create_tree(bin_tree_array_2)

    s = Solution()
    res = s.isSameTree(root_1, root_2)
    print(f" Binary trees: {bin_tree_array_1} and {bin_tree_array_2} are the same:  {res}")
