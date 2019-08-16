# -*- coding: utf-8 -*-
"""
Created on

@author: xiaoheizai
"""

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        le = ri = 0
        window = set()
        ans = [0, 0]
        while ri < lens:
            while ri < lens and s[ri] in window:
                window.remove(s[le])
                le += 1
            window.add(s[ri])
            if len(window) > ans[1] - ans[0] + 1:
                ans[0], ans[1] = le, ri
            ri += 1
        if s == "":
            return 0
        else:
            return ans[1] - ans[0] + 1