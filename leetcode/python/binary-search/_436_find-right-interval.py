#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _436_find-right-interval.py
Author       : miaoyc
Create date  : 2022/5/20 22:17
Description  : 寻找右区间
"""

"""
难度：中等

给你一个区间数组 intervals，其中intervals[i] = [starti, endi]，且每个starti都不同。
区间i的右侧区间可以记作区间 j ，并满足startj >= endi ，且startj最小化。
返回一个由每个区间 i 的右侧区间在intervals中对应下标组成的数组。如果某个区间i不存在对应的右侧区间，则下标i处的值设为-1。

示例 1：
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。

示例 2：
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。

提示：
1 <=intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
每个间隔的起点都 不相同
"""

import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        解题思路：
        1.用数组存二维数组第一列，用map存二维数组第一列以及对应的下标
        2.将数组排序，并且取出来数组最后一个max数
        3.拿每一个区间的right数去和max比较，如果大于max，说明右区间不存在，直接-1。否则存在，那么就去数组中用二分法查找那个符合要求的数字，找到之后，再去map中取下标。

        代码技巧：
        python的bisect包为内置的二分查找包
        bisect.bisect()返回查找元素下标的right
        bisect.bisect_left()返回查找元素下标的left
        bisect.bisect_right()返回查找元素下标的right
        """

        # 1.
        l, d = [], {}
        for i, interval in enumerate(intervals):
            l.append(interval[0])
            d[interval[0]] = i
        print(l, d)

        # 2.
        l = sorted(l)
        max_v = l[-1]

        # 3.
        res = []
        for _, right in intervals:
            if right > max_v:
                res.append(-1)
                continue
            index = bisect.bisect_left(l, right)
            res.append(d[l[index]])
        return res
