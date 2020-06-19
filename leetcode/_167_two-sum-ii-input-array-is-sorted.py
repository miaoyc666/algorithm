#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _167_two-sum-ii-input-array-is-sorted.py
Author       : miaoyc1989@hotmail.com
Create date  : 2020/6/19
Description  : 先二分再双指针
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


