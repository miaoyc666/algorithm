#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File name    : _1_two-sum.py
Author       : miaoyc1989@hotmail.com
Create date  : 2020/6/18
Description  :
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for index, v in enumerate(nums):
            dest = target - v
            if dest in tmp:
                return [tmp[dest], index]
            tmp[v] = index