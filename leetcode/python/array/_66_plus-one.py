#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _66_plus-one.py
Author       : miaoyc
Create date  : 2021/8/15 23:53
Description  : 加一
"""

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
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

"""
2021.9.6 补充：二刷时发现原来的逻辑写的和屎一样，是理解错了题意，我理解的是给每一位加一，实际上是给整个数组所表示的数字加一
新的解题思路：
反向遍历数组，依次取元素加一，可能出现以下三种情况：
1.末位数据不是9，末位加一，前面所有数字保持不变；
2.末位数据是9，但非全部数据都是9，末位数字加一后进位，循环向前走，依次类推；
3.所有数字都是9，数组长度加1，第一位是1，其余位数皆为0
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
