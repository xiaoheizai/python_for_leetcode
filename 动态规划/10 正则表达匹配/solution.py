# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], "."}
        
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p) 
        else:
            return self.isMatch(s[1:], p[1:]) and first_match
			
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def helper(i, j):
            if (i, j) in memo: 
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and p[j] in {s[i], "."}
            if j + 1 < len(p) and p[j+1] == "*":
                ans =  helper(i, j+2) or first_match and helper(i+1, j) 
            else:
                ans = first_match and helper(i+1, j+1) 
            memo[(i, j)] = ans
            return ans
			
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in [s[i], "."]
                if j + 1 < len(p) and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
            
        return dp[0][0]