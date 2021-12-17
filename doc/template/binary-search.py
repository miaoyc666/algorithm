#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : binary-search.py
Author       : miaoyc
Create date  : 2021/12/18 12:21 上午
Description  : 二分查找问题模板
"""


class Solution:

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 首先找到起始位置
        low = 0
        high = len(nums) - 1
        # 再设置退出条件
        while low <= high:
            # 二分条件
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low
