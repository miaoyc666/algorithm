#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1_two-sum.py
Author       : miaoyongchao@qianxin.com
Create date  : 2020/6/18
Description  : 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for index, v in enumerate(nums):
            dest = target - v
            if dest in tmp:
                return [tmp[dest], index]
            tmp[v] = index
