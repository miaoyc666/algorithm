#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _473_matchsticks-to-square.py.py
Author       : miaoyc
Create date  : 2022/6/1 17:13
Description  : 火柴拼正方形
"""

"""
难度：中等

你将得到一个整数数组matchsticks，其中matchsticks[i]是第i个火柴棒的长度。你要用所有的火柴棍拼成一个正方形。
你不能折断任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

示例1:
输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例2:
输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。


提示:
1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
"""

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = len(matchsticks)
        total = sum(matchsticks)

        # 目标是找出 把所有火柴 分成【四等份】 的组合
        target = total // 4
        if total % 4 != 0 or size < 4:  # 特判
            return False
        # 降序排列 可以加速回溯过程
        arr = sorted(matchsticks, reverse=True)

        # 如果最长的火柴 超过目标，代表无法满足要求
        if arr[0] > target:
            return False

        # 前面都是特判  下面正式开始回溯
        def dfs(i, bucket):
            if i == size:  # 递归结束条件：全部火柴都能正确放入
                return True

            for j in range(4):  # 4个桶都要试一遍
                """
                选桶<重要的剪枝步骤>
                “前一个桶和当前桶火柴数一致时，可以直接跳过”
                因为对于1根火柴来讲，两个桶大小一样，再放入时没有区别
                前面那个桶放入失败，重新放入也肯定失败，故可以直接跳过
                """
                if j and bucket[j] == bucket[j - 1]:
                    continue

                # 判断是否能放
                if bucket[j] + arr[i] <= target:
                    bucket[j] += arr[i]  # 尝试放入

                    # 如果之后的放入的火柴都无问题，就不拿出
                    if dfs(i + 1, bucket):
                        return True

                    # 若之后出现无法满足的情况，就把之前放入的火柴拿出
                    # 看看能不能放到另一个桶【j+1】里
                    bucket[j] -= arr[i]

            # for循环结束
            # 四个桶都试过了，火柴i 无法放入
            # 说明是之前出错了 需要一路回退 把之前放过的 较长火柴 重排
            # 如果到最后 连最长的火柴都无法放入，说明无解
            return False
            # 具体回溯思路 参考经典回溯题“八皇后”

        # 初始4个桶为空 从最长的火柴【下标0】
        # 调用上面定义的递归函数 开始回溯
        return dfs(0, [0, 0, 0, 0])
