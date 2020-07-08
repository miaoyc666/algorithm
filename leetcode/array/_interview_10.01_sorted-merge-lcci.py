#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _interview_10.01_sorted-merge-lcci.py
Author       : miaoyc
Create date  : 2020/7/9 12:48 上午
Description  : 合并排序的数组。
"""

"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 
编写一个方法，将 B 合并入 A 并排序。初始化 A 和 B 的元素数量分别为 m 和 n。

示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:
A.length == n + m
"""


class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        i = m + n - 1
        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                A[i] = A[m-1]
                m -= 1
            else:
                A[i] = B[n-1]
                n -= 1
            i -= 1
        if m == 0:
            while n > 0:
                A[i] = B[n-1]
                n -= 1
                i -= 1
