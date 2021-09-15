#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _283_move-zeroes.py
Author       : miaoyc
Create date  : 2021/7/21 11:38 下午
Description  : 移动零
"""

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 按顺序写非零值，后面全置零。
        # 双指针，一个指针在遇到非0值时前进，另一个指针每次都前进，快慢指针。
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, n):
            nums[i] = 0


if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])
