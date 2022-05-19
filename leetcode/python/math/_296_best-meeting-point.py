#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _296_best-meeting-point.py
Author       : miaoyc
Create date  : 2022/5/19 21:35 
Description  : 最佳的碰头地点
"""

"""
难度：困难

给你一个m x n的二进制网格grid，其中 1 表示某个朋友的家所处的位置。返回 最小的 总行走距离 。
总行走距离 是朋友们家到碰头地点的距离之和。
我们将使用曼哈顿距离来计算，其中distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。


示例 1：
输入: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
输出: 6 
解释: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
    (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。

示例 2:
输入: grid = [[1,1]]
输出: 1

提示:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] ==0or1.
grid中 至少 有两个朋友
"""

from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        解题思路：
        曼哈顿距离在x和y两个方向上是独立的，只要找到所有人x坐标和y坐标的中位数即可，这个中位数的坐标就是最优结果。
        求中位数，最简单做法就是排序再取中间的下标。
        """
        s, xlist, ylist = 0, [], []
        for x, v in enumerate(grid):
            for y, vv in enumerate(v):
                if vv == 1:
                    xlist.append(x)
                    ylist.append(y)

        midx = sorted(xlist)[int(len(xlist) / 2)]
        midy = sorted(ylist)[int(len(ylist) / 2)]

        for x in xlist:
            s += abs(x - midx)
        for y in ylist:
            s += abs(y - midy)

        return s
