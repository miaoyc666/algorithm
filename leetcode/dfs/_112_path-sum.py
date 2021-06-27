#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _112_path-sum.py
Author       : miaoyc
Create date  : 2021/6/27 11:51 下午
Description  : 路径总和
"""

"""
给你二叉树的根节节root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

示例 1：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
示例 2：

输入：root = [1,2,3], targetSum = 5
输出：false
示例 3：

输入：root = [1,2], targetSum = 0
输出：false

提示：

树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def hasPathSum(self, root, targetSum):
#         """
#         :type root: TreeNode
#         :type targetSum: int
#         :rtype: bool
#         """
#         if not root:
#             return False
#         if not root.left and not root.right:
#             return targetSum == root.val
#         return self.a(root, targetSum - root.val)

#     def a(self, root, targetSum):
#         if not root:
#             return False
#         if not root.left and not root.right:
#             return targetSum == root.val
#         return self.a(root.left, targetSum - root.val) or self.a(root.right, targetSum - root.val)


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
