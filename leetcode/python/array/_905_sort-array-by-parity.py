#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _905_sort-array-by-parity.py
Author       : miaoyc
Create date  : 2022/4/28 21:32 
Description  : 按奇偶排序数组
"""

"""
难度：简单

给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
返回满足此条件的 任一数组 作为答案。

示例 1：
输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。

示例 2：
输入：nums = [0]
输出：[0]

提示：
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""


from typing import List


# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         a = []
#         b = []
#         for i in nums:
#             if i % 2 == 0:
#                 a.append(i)
#             else:
#                 b.append(i)
#         return a + b


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
