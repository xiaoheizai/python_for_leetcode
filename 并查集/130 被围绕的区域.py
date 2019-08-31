# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class UnionFind(object):
    def __init__(self, n):
        self.uf = [-1 for i in range(n)]
    
    def find(self, node):
        temp = node
        while self.uf[node] > 0:
            node = self.uf[node]
            
        while self.uf[temp] > 0:
            self.uf[temp], temp = node, self.uf[temp]
            
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return
        if self.uf[root1] < self.uf[root2]:
            self.uf[root1] += self.uf[root2]
            self.uf[root2] = root1
        else:
            self.uf[root2] += self.uf[root1]
            self.uf[root1] = root2
    
    def is_connect(self, node1, node2):
        return self.find(node1) == self.find(node2)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return board
        col = len(board[0])
        union_table = UnionFind(row * col + 1)
        virtual_node = row * col
        
        for i in range(row):
            for j in range(col):
                index = i * col + j
                if i == 0 or j == 0 or i == row -1 or j == col - 1:
                    if board[i][j] == "O":
                        union_table.union(index, virtual_node)
                if board[i][j] == "O":
                    if i < row - 1 and board[i+1][j] == "O":
                        index_down = (i+1) * col + j
                        union_table.union(index, index_down)
                    if j < col - 1 and board[i][j+1] == "O":
                        index_right = index + 1
                        union_table.union(index, index_right)
        
        for i in range(row):
            for j in range(col):
                index = i * col + j
                if i == 0 or j ==0 or i == row - 1 or j == col - 1:
                    continue
                else:
                    if not union_table.is_connect(index, virtual_node):
                        board[i][j] = "X"