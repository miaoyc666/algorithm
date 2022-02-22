#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1994_the-number-of-good-subsets.py
Author       : miaoyc
Create date  : 2022/2/22 23:53 下午
Description  : 好子集的数目
"""

"""
难度：困难

给你一个整数数组nums。如果nums的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为好子集。
比方说，如果nums = [1, 2, 3, 4]：
[2, 3]，[1, 2, 3]和[1, 3]是 好子集，乘积分别为6 = 2*3，6 = 2*3和3 = 3。
[1, 4] 和[4]不是 好子集，因为乘积分别为4 = 2*2 和4 = 2*2。
请你返回 nums中不同的好子集的数目对109 + 7取余的结果。
nums中的 子集是通过删除 nums中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。

示例 1：
输入：nums = [1,2,3,4]
输出：6
解释：好子集为：
- [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。

示例 2：
输入：nums = [4,2,3,15]
输出：5
解释：好子集为：
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
- [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。


提示：
1 <= nums.length <= 105
1 <= nums[i] <= 30
"""

"""
题目太难，先抄为敬，核心思路是枚举
"""

from typing import List
from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:

        MOD = 1_000_000_007
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        counter = Counter(nums)
        dp = [0] * (1 << len(primes))
        dp[0] = pow(2, counter[1], MOD)

        for elem, cnt in counter.items():
            if elem != 1:
                substate = 0
                for i, prime in enumerate(primes):
                    if elem % (prime * prime) == 0:
                        break

                    if elem % prime == 0:
                        substate |= (1 << i)
                else:
                    # 内层 for 循环正常退出时，执行 else 子句
                    # 若内层 for 循环由 break 语句退出时，则不执行 else 子句，之后代码会继续执行外层 for 循环
                    for state in range((1 << len(primes)) - 1, 0, -1):
                        if (state & substate) == substate:
                            dp[state] = (dp[state] + dp[state ^ substate] * cnt) % MOD

        res = sum(dp[1:]) % MOD
        return res
