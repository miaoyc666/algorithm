#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _540_single-element-in-a-sorted-array.py
Author       : miaoyc
Create date  : 2021/7/19 11:25 下午
Description  : 有序数组中的单一元素
"""

"""
难度：中等

给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10


提示:
1 <= nums.length <= 105
0 <= nums[i]<= 105
"""

"""
难度：中等

二分法解题思路：
由于是有序数组，则数字一定是成对出现的，数列会成成对相等的形态排列，唯一的不同数据会破坏成对相等的形态。

if l = 0, r = len(nums), mid = (l + r) // 2

当mid为奇数的时候，如果唯一的异常数据在mid左边，则nums[mid]与nums[mid-1]无法凑成相等的一对数据，反之可以。
当mid为偶数的时候，如果唯一的异常数据在mid左边，则nums[mid]与nums[mid-1]可以凑成相对的一对，反之不可以。

根据以上四条规则，可以使用二分法进行查找，判断nums[mid]与nums[mid ^ 1]是否相等。

代码技巧（本题解法没用上）：
当n为奇数时，n与1亦或得到的是n - 1，n ^ 1 = n - 1
当n为偶数时，n与1亦或得到的是n + 1，n ^ 1 = n + 1

题解：https://leetcode-cn.com/problems/single-element-in-a-sorted-array/solution/miaoyc-you-xu-shu-zu-zhong-de-dan-yi-yua-gvzs/
"""


from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 != 0:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left]
