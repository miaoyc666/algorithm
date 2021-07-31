#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _167_two-sum-ii-input-array-is-sorted.py
Author       : miaoyc
Create date  : 2021/7/22 12:21 上午
Description  : 两数之和 II - 输入有序数组
"""

"""
给定一个已按照 升序排列 的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。


示例 1：

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[1,3]
示例 3：

输入：numbers = [-1,0], target = -1
输出：[1,2]


提示：

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
"""


class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 先二分
        start = 0
        end = len(numbers) - 1
        while start < end - 1:
            mid = start + (end - start) / 2
            if target < numbers[mid]:
                end = mid
            elif target > numbers[mid]:
                start = mid
            else:
                end = mid
        # 再双指针
        left = 0
        right = end
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return left+1, right+1
