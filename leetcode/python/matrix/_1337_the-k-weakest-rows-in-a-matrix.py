#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1337_the-k-weakest-rows-in-a-matrix.py
Author       : miaoyc
Create date  : 2021/8/1 11:38 下午
Description  : 
"""

from typing import List

"""
给你一个大小为m* n的矩阵mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
请你返回矩阵中战斗力最弱的k行的索引，按从最弱到最强排序。
如果第i行的军人数量少于第j行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

示例 1：

输入：mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
示例 2：

输入：mat = 
[[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]

提示：

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] 不是 0 就是 1
"""


class Solution:

    def __init__(self):
        self.value_map = {}

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            self.value_map[i] = self.calc_value(mat[i])

        # 此段代码需要考虑不用sorted如何实现，抽空去看一下sorted代码
        value_order = sorted(self.value_map.items(), key=lambda x:x[1], reverse=False)
        return [i for i, j in value_order[:k]]

    def calc_value(self, list_):
        value = 0
        for i in list_:
            if i == 1:
                value += 1
            else:
                break
        return value

