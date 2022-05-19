#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _462_minimum-moves-to-equal-array-elements-ii.py.py
Author       : miaoyc
Create date  : 2022/5/19 18:50
Description  : 最少移动次数使数组元素相等 II
"""

"""
难度：中等

给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。
在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。

示例 1：
输入：nums = [1,2,3]
输出：2
解释：
只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

示例 2：
输入：nums = [1,10,2,9]
输出：16

提示：
n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 解题思路
        # 解题关键是找到中位数，证明过程：https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/solution/by-fuxuemingzhu-13z3/
        # 找到中位数后，迭代所有差值即拿到最终结果
        nums = sorted(nums)
        r, z = 0, nums[int(len(nums)/2)]
        for i in nums:
            r += abs(i - z)
        return r
