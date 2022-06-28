#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _280_wiggle-sort.py
Author       : miaoyc
Create date  : 2022/6/28 12:31 
Description  : 摆动排序 
"""

"""
难度：中等

给你一个的整数数组nums, 将该数组重新排序后使nums[0] <= nums[1] >= nums[2] <= nums[3]...
输入数组总是有一个有效的答案。

示例 1:
输入：nums = [3,5,2,1,6,4]
输出：[3,5,1,6,2,4]
解释：[1,6,2,5,3,4]也是有效的答案

示例 2:
输入：nums = [6,6,5,6,3,8]
输出：[6,6,5,6,3,8]

提示：
1 <= nums.length <= 5 * 104
0 <= nums[i] <= 104
输入的nums 保证至少有一个答案。
"""

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()为原地排序，直接改变nums的内容
        # sorted(nums)为生成新的对象作为排序后的结果，不是原地排序
        nums.sort()
        for i in range(1, len(nums) -1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
