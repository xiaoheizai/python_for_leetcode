# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 时间复杂度O(nm), 空间复杂度O(m)
class Solution(object):
    def helper(self, lengths):
        stack = [-1]
        temp_max = 0
        for i in range(len(lengths)):
            while stack[-1] != -1 and lengths[stack[-1]] > lengths[i]:
                temp = lengths[stack.pop(-1)] * (i - stack[-1] - 1)
                temp_max = max(temp_max, temp)
            stack.append(i)
            
        while stack[-1] != -1:
            temp = lengths[stack.pop(-1)] * (i - stack[-1])
            temp_max = max(temp_max, temp)
        return temp_max
            
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxarea = 0
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        dp = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != "0":
                    dp[j] += 1
                else:
                    dp[j] = 0
            maxarea = max(maxarea, self.helper(dp))
        return maxarea

# 时间复杂度O(n^2m), 空间复杂度O(mn)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxarea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
                    
                width = dp[i][j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea
		
# 时间复杂度O(nm), 空间复杂度O(m)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        elif len(matrix[0]) == 0:
            return 0
        maxarea = 0
        left = [0] * len(matrix[0])
        right = [len(matrix[0])] * len(matrix[0])
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            curleft = 0
            curright = len(matrix[0])
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    height[j] = 0
                else:
                    height[j] += 1
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curleft)
                else:
                    left[j] = 0
                    curleft = j + 1
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curright)
                else:
                    right[j] = len(matrix[0])
                    curright = j
            for j in range(len(matrix[0])):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
        return maxarea