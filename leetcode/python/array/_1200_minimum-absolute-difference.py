#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1200_minimum-absolute-difference.py
Author       : miaoyc
Create date  : 2022/7/4 22:43
Description  : 最小绝对差
"""

"""
难度：简单

给你个整数数组arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

示例 1：
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]

示例 2：
输入：arr = [1,3,6,10,15]
输出：[[1,3]]

示例 3：
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]

提示：
2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_v = arr[1] - arr[0]
        list_v = []
        for i in range(1, len(arr)):
            tmp = arr[i] - arr[i-1]
            if tmp < min_v:
                min_v = min(min_v, arr[i] - arr[i-1])
                list_v = [(arr[i-1], arr[i])]
            elif tmp == min_v:
                list_v.append((arr[i-1], arr[i]))
        return list_v
