#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _118_pascals-triangle.py
Author       : miaoyc
Create date  : 2021/7/28 10:49 下午
Description  : 杨辉三角
"""

"""
给定一个非负整数numRows，生成「杨辉三角」的前numRows行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例2:

输入: numRows = 1
输出: [[1]]


提示:

1 <= numRows <= 30

"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1, numRows + 1):
            # 先生成全是1的数组
            tmp = [1 for _ in range(i)]
            print(tmp)
            for j in range(1, len(tmp) - 1):
                # 第三行数组的第二个元素（数组下标1）需要计算，使用第二行的0和1数据相加
                # 第四行数组的第二、三个元素（数组下标1、2）需要计算，使用第三行的0、1、和2数据相加
                # i=3的时候，i-2=1代表第二行
                tmp[j] = ret[i - 2][j - 1] + ret[i - 2][j]
            ret.append(tmp)
        return ret


if __name__ == "__main__":
    print(Solution().generate(5))

