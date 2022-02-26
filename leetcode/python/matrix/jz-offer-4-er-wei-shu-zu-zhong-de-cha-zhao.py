#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-4-er-wei-shu-zu-zhong-de-cha-zhao.py
Author       : miaoyc
Create date  : 2022/1/13 12:34 上午
Description  : 二维数组中的查找
"""

"""
难度：中等

与240 search-a-2d-matrix-ii题目重复

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。
给定target=20，返回false。

限制：
0 <= n <= 1000
0 <= m <= 1000
"""

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # 每比较一次，抛弃一行或一列
        # 从右上角开始比较
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

