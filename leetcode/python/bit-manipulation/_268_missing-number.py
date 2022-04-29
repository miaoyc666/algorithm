#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _268_missing-number.py
Author       : miaoyc
Create date  : 2022/4/29 23:22
Description  : 丢失的数字
"""

"""
难度：简单

给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
nums 中的所有数字都 独一无二

进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
"""

from typing import List

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         for i, v in enumerate(nums):
#             if i != v:
#                 return i
#         return len(nums)


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         s = set(nums)
#         for i in range(len(nums) + 1):
#             if i not in s:
#                 return i

'''
空间复杂度O(1)的解法

根据出现的次数的奇偶性，可以使用按位异或运算得到丢失的数字。按位异或运算⊕满足交换律和结合律，且对任意整数x都满足x⊕x=0 和x⊕0=x。

由于上述 2n+12n+1 个整数中，丢失的数字出现了一次，其余的数字都出现了两次，因此对上述2n+1个整数进行按位异或运算，结果即为丢失的数字。
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i, v in enumerate(nums):
            xor ^= i ^ v
        return xor ^ len(nums)
