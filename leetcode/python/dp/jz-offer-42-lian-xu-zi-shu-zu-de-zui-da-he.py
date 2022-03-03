#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-42-lian-xu-zi-shu-zu-de-zui-da-he.py
Author       : miaoyc
Create date  : 2022/3/3 10:20 PM 
Description  : 连续子数组的最大和
"""

"""
难度：简单

与53 maximum-subarray题目重复
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。

提示：
1 <=arr.length <= 10^5
-100 <= arr[i] <= 100
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)

