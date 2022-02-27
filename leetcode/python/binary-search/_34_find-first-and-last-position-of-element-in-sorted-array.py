#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _34_find-first-and-last-position-of-element-in-sorted-array.py
Author       : miaoyc
Create date  : 2022/2/27 11:54 PM 
Description  : 在排序数组中查找元素的第一个和最后一个位置
"""

"""
难度：中等

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。
进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109
"""

"""
解题思路：
两次二分查找，一次找到头的索引，一次找到尾的索引
由于存在重复元素，退出条件就不再是nums[mid] == target
当查找左边界时，出现判等后，high=mid-1继续查找，最终返回low
当查找右边界时，出现判等后，low=mid+1继续查找，最终返回high
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        return [self.find_left(nums, target), self.find_right(nums, target)]

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


if __name__ == "__main__":
    a = [5, 7, 7, 8, 8, 10]
    b = 8
    print(Solution().find_left(a, b))
    print(Solution().find_right(a, b))
