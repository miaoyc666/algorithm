#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _637_average-of-levels-in-binary-tree.py
Author       : miaoyc
Create date  : 2021/7/15 11:37 下午
Description  : 二叉树的层平均值
"""

"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        queue_ = [root]
        while len(queue_) > 0:
            size = len(queue_)
            total = 0
            for i in range(size):
                head = queue_.pop(0)
                total += head.val
                if head.left:
                    queue_.append(head.left)
                if head.right:
                    queue_.append(head.right)
            avg = total * 1.0 / size
            result.append(avg)
        return result
