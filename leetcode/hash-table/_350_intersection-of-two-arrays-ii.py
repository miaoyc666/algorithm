#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _350_intersection-of-two-arrays-ii.py
Author       : miaoyc
Create date  : 2021/7/26 23:23
Description  : 两个数组的交集 II
"""

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果nums1的大小比nums2小很多，哪种方法更优？
如果nums2的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        tmp = {}
        for i in nums1:
            if i not in tmp:
                tmp[i] = 0
            tmp[i] += 1

        res = []
        for i in nums2:
            if i in tmp:
                res.append(i)
                tmp[i] -= 1
                if tmp[i] == 0:
                    del tmp[i]
        return res
