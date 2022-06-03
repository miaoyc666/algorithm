#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _453_minimum-moves-to-equal-array-elements.py.py
Author       : miaoyc
Create date  : 2022/5/19 19:21
Description  : 最小操作次数使数组元素相等
"""

"""
难度：简单

给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

示例 1：
输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

示例 2：
输入：nums = [1,1,1]
输出：0

提示：
n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
答案保证符合 32-bit 整数
"""

from typing import List

"""
解题思路：
n-1个数同时+1，相当于每次有1个数自身-1，因为只能做减法，所以数组最后的数只能是最小值。因此，每个元素减去最小值求其和就是答案。
"""


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s, m = 0, min(nums)
        for i in nums:
            s += abs(i - m)
        return s
