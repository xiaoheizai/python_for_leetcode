# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        levels = []
        bi_queue = deque([root])
        level = 0
        while bi_queue:
            levels.append([])
            length = len(bi_queue)
            for _ in range(length):
                node = bi_queue.popleft()
                if node.left is not None:
                    bi_queue.append(node.left)
                if node.right is not None:
                    bi_queue.append(node.right)
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].insert(0, node.val)
            level += 1
        return levels