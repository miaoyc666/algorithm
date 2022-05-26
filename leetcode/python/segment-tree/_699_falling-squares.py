#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _699_falling-squares.py
Author       : miaoyc
Create date  : 2022/5/26 12:28 
Description  : 掉落的方块
"""

"""
难度：困难

在二维平面上的 x 轴上，放置着一些方块。
给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点lefti 对齐。
每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。
在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。
返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。

示例 1：
输入：positions = [[1,2],[2,3],[6,1]]
输出：[2,5,5]
解释：
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
因此，返回 [2, 5, 5] 作为答案。

示例 2：
输入：positions = [[100,100],[200,100]]
输出：[100,100]
解释：
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
因此，返回 [100, 100] 作为答案。
注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。

提示：
1 <= positions.length <= 1000
1 <= lefti <= 108
1 <= sideLengthi <= 106
"""

"""
解题思路：
1.看不懂，先抄个题解： https://leetcode.cn/problems/falling-squares/solution/-by-lcbin-5rop/
"""

from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        mx = 0
        tree = SegmentTree()
        for l, w in positions:
            r = l + w - 1
            h = tree.query(l, r) + w
            mx = max(mx, h)
            ans.append(mx)
            tree.modify(l, r, h)
        return ans


class Node:
    def __init__(self, l, r):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = 0
        self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = v
            node.add = v
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v = max(v, self.query(l, r, node.left))
        if r > node.mid:
            v = max(v, self.query(l, r, node.right))
        return v

    def pushup(self, node):
        node.v = max(node.left.v, node.right.v)

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            node.left.v = node.add
            node.right.v = node.add
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0
