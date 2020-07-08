#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _167_two-sum-ii-input-array-is-sorted.py
Author       : miaoyc
Create date  : 2020/6/19
Description  : 先二分再双指针
"""

"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 二分
        start = 0
        end = len(numbers) - 1
        while start < end - 1:
            mid = start + (end - start) / 2
            print mid, start, end
            if target < numbers[mid]:
                end = mid
            elif target > numbers[mid]:
                start = mid
            else:
                end = mid
        # 双指针
        left = 0
        right = end
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return left+1, right+1


