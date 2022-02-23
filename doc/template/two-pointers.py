#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : two-pointers.py
Author       : miaoyc
Create date  : 2022/2/23 9:44 PM 
Description  : 双指针模板
"""

from typing import List


class Solution:

    def action(self, num):
        """遍历节点后的操作"""
        print(num)

    def two_points_scan(self, nums: List[int]) -> int:
        """
        双指针问题首尾面对面碰撞模板
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if self.action(left):
                left += 1
            if self.action(right):
                right -= 1
        return 0
