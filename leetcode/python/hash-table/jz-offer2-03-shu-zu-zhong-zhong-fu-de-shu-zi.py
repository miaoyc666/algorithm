#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer2-03-shu-zu-zhong-zhong-fu-de-shu-zi.py
Author       : miaoyc
Create date  : 2022/1/6 10:57 下午
Description  : 数组中的重复数字
"""

"""
难度：简单

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

限制：
2 <= n <= 100000
"""

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        tmp = set()
        for i in nums:
            if i not in tmp:
                tmp.add(i)
            else:
                return i
