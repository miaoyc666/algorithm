#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : can-i-win.py
Author       : miaoyc
Create date  : 2022/5/22 15:01
Description  : 我能赢吗
"""

"""
难度：中等

在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过 100 的玩家，即为胜者。
如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？
例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
给定两个整数maxChoosableInteger（整数池中可选择的最大数）和desiredTotal（累计和），若先出手的玩家是否能稳赢则返回 true，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

示例 1：
输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

示例 2:
输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true

示例 3:
输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true

提示:
1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""

"""
解题思路：
1、
2、
"""

from functools import cache


class Solution:
    def canIWin(self, max_choosable_integer: int, desired_total: int) -> bool:
        @cache
        def dfs(used_numbers: int, current_total: int) -> bool:
            for i in range(max_choosable_integer):
                if (used_numbers >> i) & 1 == 0:
                    if current_total + i + 1 >= desired_total or not dfs(used_numbers | (1 << i), current_total + i + 1):
                        return True
            return False

        return (1 + max_choosable_integer) * max_choosable_integer // 2 >= desired_total and dfs(0, 0)
