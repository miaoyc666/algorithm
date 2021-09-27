#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _169_majority-element.py
Author       : miaoyc
Create date  : 2021/9/27 11:45 下午
Description  : 多数元素
"""

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例1：
输入：[3,2,3]
输出：3

示例2：
输入：[2,2,1,1,1,2,2]
输出：2

进阶：
尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for k, v in dic.items():
            if v >= len(nums)/2:
                return k
        return -1
