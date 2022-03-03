#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-zi.py
Author       : miaoyc
Create date  : 2022/2/27 12:31 AM 
Description  : 寻找旋转数组的最小值II
"""

"""
难度：困难

与154 find-minimum-in-rotated-sorted-array-ii题目重复

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
给你一个可能存在重复元素值的数组numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        解题思路：
        此题与旋转无重复数据的排序数组中最小值的唯一区别为存在重复值，解决方法是在二分查找时判断等于的条件，当等于时，不再二分，而已减一。
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]
