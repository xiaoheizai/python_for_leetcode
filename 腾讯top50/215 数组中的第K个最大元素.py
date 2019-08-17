# -*- coding: utf-8 -*-
"""
Created on Apr 13、4

@author: xiaoheizai
"""

'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def creat_heap(self, nums):
        lens = len(nums)
        last_node = (lens -2 ) // 2
        i = last_node
        while i >= 0:
            stack = [i]
            while len(stack) > 0:
                j = stack.pop()
                if 2 * j + 2 < lens and nums[2 * j + 1] > nums[2 * j + 2]:
                    may_index = 2 * j + 2
                else:
                    may_index = 2 * j + 1
                if nums[may_index] < nums[i]:
                    nums[i], nums[may_index] = nums[may_index], nums[i]
                if may_index <= last_node:
                    stack.append(may_index)
            i -= 1
        
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lens = len(nums)
        temp_list = nums[:k]
        self.creat_heap(temp_list)
        for i in range(k, lens):
            if nums[i] > temp_list[0]:
                temp_list[0] = nums[i]
                self.creat_heap(temp_list)
        return temp_list[0]
        