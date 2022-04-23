#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _18_4sum.py
Author       : miaoyc
Create date  : 2022/4/23 23:49
Description  : 四数之和
"""

"""
难度：中等

给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]（若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

提示：
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

"""
解题思路：
在三数之和的基础上再多一层循环，n数之和的解法以此类推。
"""