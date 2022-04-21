#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _15_3sum.py
Author       : miaoyc
Create date  : 2022/3/16 6:13 PM 
Description  : 三数之和
"""

"""
难度：中等

给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]

提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

"""
解题思路：
1.先对数组排序，得到有序数组nums；
2.双层遍历nums，每次遍历的数据为a（注意要跳过重复数据），需要在剩余数组（nums1）中找到的数据为b和c，target - a = b + c；
3.遍历有序数组nums1，使用双指针遍历（注意要跳过重复数据），时间复杂度为O(n)；
4.步骤三中找到b和c后，结合步骤2中使用的a，即可得到一组答案[a,b,c]；

时间复杂度: O(N^N)
时间复杂度分析：数组排序O(NlogN)，遍历数组O(N)，双指针遍历O(N)，总体为：O(NlogN) + O(N)*O(N) = O(N*N) 
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        三数之和
        解题思路：
        1.先对数组排序，得到有序数组nums；
        2.双层遍历nums，每次遍历的数据为nums[a]（注意要跳过重复数据），需要在剩余数组（nums1）中找到的数据为nums[b]和nums[c]，target - nums[a] = nums[b] + nums[c], a、b和c为数组下标索引，a < b < c；
        3.遍历有序数组nums1，使用双指针遍历（注意要跳过重复数据），时间复杂度为O(n)；
        4.步骤三中找到b和c后，结合步骤2中使用的a，即可得到一组答案[nums[a],nums[b],nums[c]]；

        时间复杂度: O(N^N)
        时间复杂度分析：数组排序O(NlogN)，遍历数组O(N)，双指针遍历O(N)，总体为：O(NlogN) + O(N)*O(N) = O(N*N)
        """
        nums = sorted(nums)
        length = len(nums)
        result = []
        for a in range(length):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            target = -nums[a]
            # 双指针遍历数组求和（nums[b]+nums[c]=target），索引b为左指针，索引c为右指针
            c = length - 1
            for b in range(a+1, length):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    result.append([nums[a], nums[b], nums[c]])
        return result
