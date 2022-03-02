#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-32-III-cong-shang-dao-xia-da-yin-er-cha-shu-iii.py
Author       : miaoyc
Create date  : 2022/3/1 12:19 AM 
Description  : 从上到下打印二叉树III
"""

"""
难度：中等

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树:[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]

提示：
节点总数 <= 1000
"""

from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.queue_ = []
        self.result = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :param root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.queue_, self.result = [root], [[root.val]]
        # 使用n作为标识，来标记当前遍历的是奇数层还是偶数层
        n = 1
        while len(self.queue_) > 0:
            n += 1
            size = len(self.queue_)
            layer = deque()
            for i in range(size):
                head = self.queue_.pop(0)
                if head.left:
                    self._append(n, layer, head.left)
                if head.right:
                    self._append(n, layer, head.right)
            if len(layer) != 0:
                self.result.append(list(layer))

        return self.result

    def _append(self, n, layer, node):
        if n % 2 != 0:
            layer.append(node.val)
        else:
            layer.appendleft(node.val)
        self.queue_.append(node)
