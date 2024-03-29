#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _189_rotate-array.py
Author       : miaoyc
Create date  : 2021/7/21 2:54
Update date  : 2024/1/9 12:58
Description  : 旋转数组
"""

"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

提示：
1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？
"""


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 这种题用库函数多没意思
        n = len(nums)
        k = k % n
        # 全部翻转
        for i in range(int(n/2)):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]

        # 翻转0~k
        for i in range(0, int(k/2)):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        # 翻转k到n
        for i in range(k, int((n+k)/2)):
            nums[i], nums[n+k-1-i] = nums[n+k-1-i], nums[i]
        