# -*- coding: utf-8 -*-
"""
Created on Apr 17

@author: xiaoheizai
"""

'''
description:
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
火车票有三种不同的销售方式：
一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，
那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释： 
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。

输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
你总共花了 $17，并完成了你计划的每一天旅行。

动态规划：用dp[n]来记录365天里第n天需要花费的时间，那么它的花费可以是
1）dp[n-1]的花费加上第n天的花费costs[0]
2）dp[n-7]的花费加上连续七天的花费costs[1]
3）dp[n-30]的花费加上连续三十天的花费costs[2]
取三个值最小的就是第n天花费最小的费用

约束条件：
没有出现在days中的日期j , 花费应该和之前旅行花费的费用一样
dp[0]是第0天，费用应该是0元
'''


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        i = 0
        length = len(days)
        while i < length:
            value = days[i]
            temp_index = value - 7
            temp_index_2 = value - 30
            if temp_index < 0:
                temp_index = 0
            if temp_index_2 < 0:
                temp_index_2 = 0
            cost = min([dp[value-1] + costs[0], dp[temp_index] + costs[1], 
                        dp[temp_index_2] + costs[2]])
            dp[value] = cost
            if i + 1 < length:
                next_index = days[i+1]
            else:
                next_index = days[i]
            for j in range(value+1, next_index):
                dp[j] = cost
            i += 1
        return dp[next_index]