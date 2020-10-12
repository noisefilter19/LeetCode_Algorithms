# Problem link:
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

'''
Approach - the idea here is to print each level, but the direction changes at
each level. While adding nodes to a queue (like in BFS), we add a delimiter
that helps us track when a level is ending, and change the direction of
traversal for a level. 
We use a deque since appending and popping on either end is O(1). More on
deque: https://docs.python.org/3/library/collections.html#collections.deque
'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # empty binary tree (edge case)
        if not root:
            return []
        # we want to do bfs here, but the direction of traversal will change
        # after every level (use delimiter for that), using a variable to
        # track direction
        zigzagLevelOrderTraversal = []
        # a deque supports faster append operation from both sides
        zigzagLevel = deque()
        bfsQueue = deque()
        leftToRight = True  # change at every level
        # using an integer delimiter since all other elements in deque will be
        # TreeNode objects
        delimiter = -1
        bfsQueue.append(root)
        bfsQueue.append(delimiter)
        while bfsQueue:
            node = bfsQueue.popleft()
            if node == delimiter:
                zigzagLevelOrderTraversal.append(zigzagLevel)
                # we only proceed further if bfsQueue is not empty
                if bfsQueue:
                    # change leftToRight since level is changing
                    leftToRight = False if leftToRight else True
                    zigzagLevel = deque()   # empty current level elements
                    bfsQueue.append(delimiter)
            else:
                if leftToRight:
                    zigzagLevel.append(node.val)
                else:
                    zigzagLevel.appendleft(node.val)
                if node.left:
                    bfsQueue.append(node.left)
                if node.right:
                    bfsQueue.append(node.right)
        return zigzagLevelOrderTraversal
