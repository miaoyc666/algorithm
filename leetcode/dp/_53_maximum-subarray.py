#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _53_maximum-subarray.py
Author       : miaoyc
Create date  : 2020/7/10 5:39 下午
Description  : 最大子序和
"""

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
