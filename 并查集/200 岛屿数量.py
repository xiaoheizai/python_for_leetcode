# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class UnionFind(object):
    def __init__(self, n):
        self.uf = [-1 for i in range(n)]
        self.count = n
        
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
        elif self.uf[root1] < self.uf[root2]:
            self.uf[root1] += self.uf[root2]
            self.uf[root2] = root1
        else:
            self.uf[root2] += self.uf[root1]
            self.uf[root1] = root2
        self.count -= 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        virtual_node = row * col
        union_table = UnionFind(row*col + 1)
        for i in range(row):
            for j in range(col):
                index = i * col + j
                if grid[i][j] == "0":
                    union_table.union(index, virtual_node)
                elif grid[i][j] == "1":
                    if i < row - 1 and grid[i+1][j] == "1":
                        index_down = (i + 1) * col + j
                        union_table.union(index, index_down)
                    if j < col - 1 and grid[i][j+1] == "1":
                        index_right = index + 1
                        union_table.union(index, index_right)
        return union_table.count - 1