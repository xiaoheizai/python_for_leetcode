# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
description:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

动态规划求解：
设置p[n]表示字符串s[:n]（这里字符串不会取到右侧的第n个字符）是否可以被拆分为字典中的词，是标记True，否标记False
s = "leetcode", wordDict = ["leet", "code"]
判断s[:4] = "leet"是否可以被划分为字典中的词，则遍历字典中的词：
1）对于字典中的词"code"，应该做以下三个条件判断
   s[4-len(code):4] == "code" and p[4-len(code)] = True and 4 - len(code) >= 0
   显然第一个条件就不符合，因而遍历下一个词
2）对于字典中的词“leet”，同样做以下三个条件判断
	s[4-len(leet):4] == "leet" and p[4-len(leet)] = True and 4 - len(leet) >= 0
	显然当p[0]=True,则三个条件成立，而p[0]=True是初始条件，从实际出发，我们知道应该设置为True
	因而p[4] = True

直到判断s[:8] = "leetcode"是否可以被划分为字典中的词，则遍历字典中的词：
1)对于字典中的词“code”，应该做以下三个条件判断
   s[8-len(code):] == "code" and p[8-len(code)] = True and 8 - len(code) >= 0
   显然第二个条件p[4]在n=4已经判断过了，为True
   因而三个条件均成立，p[8]为True，退出

返回p[-1]
'''

# 动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        p = [False] * (len(s)+1)
        p[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                length = len(word)
                if i - length >= 0 and s[i-length:i] == word and p[i-length] == True:
                    p[i] = True
                    break
        return p[-1]
		
# 字典树，还未通过
class Node:
    def __init__(self):
        self.next = {}
        self.end = False
        
class Dict_tree:
    def __init__(self, word_list):
        self.root = Node()
        for word in word_list:
            temp_node = self.root
            for value in word:
                try:
                    temp_node = temp_node.next[value]
                except KeyError:
                    temp_node.next[value] = Node()
                    temp_node = temp_node.next[value]
            temp_node.end = True
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_root = Dict_tree(wordDict).root
        p = [("", s)]
        temp_node = dict_root
        while len(p) != 0 and p[0][1] != "":
            s1, s2 = p.pop(0)
            for i in range(len(s2)):
                value = s[i]
                try:
                    temp_node = temp_node.next[value]
                    if temp_node == True:
                        s1 = s[:i+1]
                        if i+1 == len(s):
                            s2 = ""
                        else:
                            s2 = s[i+1:]
                        p.append((s1, s2))
                except KeyError:
                    break
        if len(p) != 0:
            return True
        else:
            return False