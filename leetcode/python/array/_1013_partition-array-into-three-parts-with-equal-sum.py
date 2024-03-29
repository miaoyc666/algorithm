#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1013_partition-array-into-three-parts-with-equal-sum.py
Author       : miaoyc
Create date  : 2020/7/23 12:21 上午
Description  : 将数组分成和相等的三个部分
"""

"""
给你一个整数数组A，只有可以将其划分为三个和相等的非空部分时才返回true，否则返回 false。
形式上，如果可以找出索引i+1 < j且满足A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]就可以将数组三等分。

示例 1：
输入：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


提示：
3 <= A.length <= 50000
-10^4<= A[i] <= 10^4
"""


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        target = sumA / 3
        tmp_value, sign = 0, 0
        for i in range(len(A)):
            tmp_value += A[i]
            if tmp_value == target:
                sign += 1
                tmp_value = 0
                if sign == 2 and sum(A[i+1:]) == target and i != len(A)-1:
                    return True
        return False
