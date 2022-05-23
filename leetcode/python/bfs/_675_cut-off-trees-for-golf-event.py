#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _675_cut-off-trees-for-golf-event.py
Author       : miaoyc
Create date  : 2022/5/23 22:55
Description  : 为高尔夫比赛砍树
"""

"""
难度：困难

你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个m x n 的矩阵表示， 在这个矩阵中：
0 表示障碍，无法触碰
1表示地面，可以行走
比 1 大的数表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

示例 1：
输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。

示例 2：
输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。

示例 3：
输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。

提示：
m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
"""

"""
解题思路：
看不懂，cv睡觉
"""

from typing import List
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx: int, sy: int, tx: int, ty: int) -> int:
            m, n = len(forest), len(forest[0])
            q = deque([(0, sx, sy)])
            vis = {(sx, sy)}
            while q:
                d, x, y = q.popleft()
                if x == tx and y == ty:
                    return d
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] and (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((d + 1, nx, ny))
            return -1

        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        ans = preI = preJ = 0
        for _, i, j in trees:
            d = bfs(preI, preJ, i, j)
            if d < 0:
                return -1
            ans += d
            preI, preJ = i, j
        return ans
