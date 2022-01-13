#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _46_permutations.py
Author       : miaoyc
Create date  : 2022/1/14 12:08 上午
Description  : 全排列
"""

"""
难度：中等

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""

"""
解题思路：
1.递归遍历数组 
2.递归传参使用索引，不要直接传递列表对象，会内存膨胀
3.执行完一次递归操作后，进行替换数组元素位置的撤销操作
"""

from typing import List


class Solution:

    def __init__(self):
        self.size = 0
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first):
            if first == self.size:
                self.res.append(nums[:])
            for i in range(first, self.size):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        self.size = len(nums)
        backtrack(0)
        return self.res
