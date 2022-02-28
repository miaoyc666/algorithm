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

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :param root:
        :return:
        """
        pass
    