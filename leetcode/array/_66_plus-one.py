#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _66_plus-one.py
Author       : miaoyc
Create date  : 2021/8/15 23:53
Description  : 加一
"""

"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]

提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            if digits[0] == 9:
                return [1, 0]
            else:
                digits[0] += 1
                return digits

        for i in range(len(digits)-1, -1, -1):
            if i == 0:
                if digits[i] == 10:
                    digits[i] = 0
                    digits = [1] + digits
                break
            if i == len(digits)-1:
                if digits[i] + 1 == 10:
                    digits[i] = 0
                    digits[i-1] += 1
                else:
                    digits[i] += 1
                continue

            if digits[i] + 1 > 10:
                digits[i] = 0
                digits[i-1] += 1
        return digits
