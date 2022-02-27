#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-53-I-zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi.py
Author       : miaoyc
Create date  : 2022/2/28 12:52 AM 
Description  : 在排序数组中查找数字 I
"""

"""
难度：中等

与34 find-first-and-last-position-of-element-in-sorted-array题目重复
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

提示：
0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return 0
        return len(nums[self.find_left(nums, target): self.find_right(nums, target)+1])

    def find_left(self, nums: List[int], target: int):
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

