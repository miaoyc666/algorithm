#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _977_squares-of-a-sorted-array.py
Author       : miaoyc
Create date  : 2021/7/20 11:38 下午
Description  : 有序数组的平方
"""

"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序

进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题
"""


class Solution(object):

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * len(nums)

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] ** 2 >= nums[j] ** 2:
                result[pos] = nums[i] ** 2
                i += 1
            elif nums[i] ** 2 < nums[j] ** 2:
                result[pos] = nums[j] ** 2
                j -= 1
            pos -= 1
        return result


if __name__ == "__main__":
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
