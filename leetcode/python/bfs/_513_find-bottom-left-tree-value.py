#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _513_find-bottom-left-tree-value.py
Author       : miaoyc
Create date  : 2022/6/22 22:50
Description  : 找树左下角的值
"""

"""
难度：中等

给定一个二叉树的 根节点 root，请找出该二叉树的最底层最左边节点的值。
假设二叉树中至少有一个节点。

示例 1:
输入: root = [2,1,3]
输出: 1

示例 2:
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7

提示:
二叉树的节点个数的范围是 [1,104]
-231<= Node.val <= 231- 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue_ = [root]
        while len(queue_) > 0:
            size = len(queue_)
            for i in range(size):
                head = queue_.pop(0)
                if head.right:
                    queue_.append(head.right)
                if head.left:
                    queue_.append(head.left)
        return head.val
