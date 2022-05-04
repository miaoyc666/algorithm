#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _179_largest-number.py
Author       : miaoyc
Create date  : 2022/1/16 2:19 上午
Description  : 最大数
"""

"""
难度：中等

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""

"""
解题思路：自定义排序
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)
        return logs
