#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1480_running-sum-of-1d-array.py
Author       : miaoyc
Create date  : 2020/6/30
Description  : 直接遍历即可
"""

"""
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums[0:i+1]) for i in range(len(nums))]
