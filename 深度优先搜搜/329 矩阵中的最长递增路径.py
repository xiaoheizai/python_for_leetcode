# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def dfs(self, i, j, row, col, matrix, flags, dp):
        if flags[i][j] == 1:
            return dp[i][j]
        if i + 1 < row and matrix[i+1][j] > matrix[i][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i+1, j, row, col, matrix, flags, dp)+1)
        if j + 1 < col and matrix[i][j+1] > matrix[i][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i, j+1, row, col, matrix, flags, dp)+1)
        if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i-1, j, row, col, matrix, flags, dp)+1)
        if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i, j-1, row, col, matrix, flags, dp)+1)
        flags[i][j] = 1
        return dp[i][j]
        
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix and matrix[0]:
            row = len(matrix)
            col = len(matrix[0])
        else:
            return 0
        dp = [[1] * col for _ in range(row)]
        flags = [[0] * col for _ in range(row)]
        max_length = 0
        for i in range(row):
            for j in range(col):
                temp_length = self.dfs(i, j, row, col, matrix, flags, dp)
                if temp_length > max_length:
                    max_length = temp_length
        return max_length
