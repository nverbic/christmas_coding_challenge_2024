"""
Challenge 226. 

Given the root of a binary tree, invert the tree, and return its root.

Running in main():
Binary tree: [1, 2, 3, 4, 5, 11, 12]
Inverted binary tree
1
3
2
12
11
5
4
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        start = deque()
        start.append(root)

        while start:
            for _ in range(len(start)):
                node = start.popleft()
                if node:
                    if node.left:
                        temp_left = node.left
                    else:
                        temp_left = None

                    if node.right:
                        node.left = node.right
                    else:
                        node.left = None

                    node.right = temp_left
                    start.append(node.left)
                    start.append(node.right)

        return root

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
    bin_tree_array = [1,2,3,4,5,11,12]
    root = create_tree(bin_tree_array)

    s = Solution()
    res = s.invertTree(root)
    print(f" Binary tree: {bin_tree_array}")

    print(f"Inverted binary tree")
    queue = [res]
    result = []

    while queue:
        l = queue.pop(0)
        result.append(l)

        if l.left:
            queue.append(l.left)
        if l.right:
            queue.append(l.right)

    for i in range(len(result)):
        print(result[i].val)