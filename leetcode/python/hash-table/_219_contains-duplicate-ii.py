#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _219_contains-duplicate-ii.py
Author       : miaoyc
Create date  : 2022/4/9 23:46
Description  : 存在重复元素 II
"""

"""
难度：简单

给你一个整数数组nums 和一个整数k ，判断数组中是否存在两个 不同的索引i和j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

示例1：
输入：nums = [1,2,3,1], k = 3
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true

示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false

提示：
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False
