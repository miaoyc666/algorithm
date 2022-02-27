#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : binary-search.py
Author       : miaoyc
Create date  : 2021/12/18 12:21 上午
Description  : 二分查找问题模板
"""

from typing import List


class Solution:

    def binary_search(self, nums, target):
        """
        查找到目标既返回mid
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 首先找到起始位置
        low, high = 0, len(nums) - 1
        # 再设置退出条件
        while low < high:
            # 二分条件
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def find_left(self, nums: List[int], target: int):
        """
        查找左边界
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 如果 nums[mid] = target，继续向左寻找左边界
            if nums[mid] == target:
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[low] == target:
            return low
        else:
            return -1

    def find_right(self, nums: List[int], target: int):
        """
        查找右边界
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            # 如果 nums[mid] = target，继续向右寻找右边界
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[high] == target:
            return high
        else:
            return -1
