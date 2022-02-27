#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _154_find-minimum-in-rotated-sorted-array-ii.py
Author       : miaoyc
Create date  : 2022/1/7 12:13 上午
Description  : 寻找旋转数组的最小值II
"""

"""
难度：困难， 实现不难，思路不好想

已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

示例 1：
输入：nums = [1,3,5]
输出：1

示例 2：
输入：nums = [2,2,2,0,1]
输出：0

提示：
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

进阶：
这道题是寻找旋转排序数组中的最小值的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
"""

from typing import List

"""
解题思路：
运用二分法
原题是升序数组，那么当中间值小于
"""


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
