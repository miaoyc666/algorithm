#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1748_sum-of-unique-elements.py
Author       : miaoyc
Create date  : 2022/2/6 11:54 下午
Description  : 唯一元素的和
"""

"""
难度：简单

给你一个整数数组nums。数组中唯一元素是那些只出现恰好一次的元素。
请你返回nums中唯一元素的和。

示例 1：
输入：nums = [1,2,3,2]
输出：4
解释：唯一元素为 [1,3] ，和为 4 。

示例 2：
输入：nums = [1,1,1,1,1]
输出：0
解释：没有唯一元素，和为 0 。
示例 3 ：

输入：nums = [1,2,3,4,5]
输出：15
解释：唯一元素为 [1,2,3,4,5] ，和为 15 。

提示：
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

# 简单题重拳出击吧
from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num, cnt in Counter(nums).items() if cnt == 1)
