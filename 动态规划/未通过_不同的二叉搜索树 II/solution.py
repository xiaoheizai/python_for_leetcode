# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   

'''


import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        tree_list = []
        node_1 = TreeNode(1)
        tree_list.append(node_1)
        for i in range(2, n+1):
            new_list = []
            last_list = []
            for node_value in tree_list:
                temp_list = []
                # 新插入的值在现有二叉树的节点
                temp_node = copy.deepcopy(node_value)
                temp_root = temp_node
                while temp_node.right != None:
                    temp_value = copy.deepcopy(node_value)
                    temp_value_right = temp_value.right
                    temp_value.right = TreeNode(i)
                    temp_value.right.left = temp_value_right
                    temp_list.insert(0, temp_value)
                    temp_node = temp_node.right
                temp_node.right = TreeNode(i)
                temp_list.insert(0, temp_root)
                new_list.extend(temp_list)
                # 新插入的值为顶点
                temp_value = copy.deepcopy(node_value)
                new_root = TreeNode(i)
                new_root.left = temp_value
                last_list.append(new_root)
            new_list.extend(last_list)
            tree_list = new_list
        return tree_list