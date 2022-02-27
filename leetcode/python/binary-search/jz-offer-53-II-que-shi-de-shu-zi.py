#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-53-II-que-shi-de-shu-zi.py
Author       : miaoyc
Create date  : 2022/2/28 1:14 AM 
Description  : 缺失的数字
"""

"""
难度：简单

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

限制：
1 <= 数组长度 <= 10000
"""

"""
解题思路：
只要比较数组下标和该下标对应的值即可，再排除缺失0和缺失最后一项两个特殊情况。
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # 左闭右闭区间
        while low <= high:
            mid = low + (high - low) // 2
            """
            左子数组：nums[i] = i
            右子数组：nums[i] != i
            当中间元素跟索引相等，那就应该去右子数组中查
            如果不等的话，就去找左子数组中查找，因为我们本质上是要找不相等的第1个（或者说最左边的那个）
            """
            if nums[mid] == mid:
                low = mid + 1
            else:
                high = mid - 1
        return low
