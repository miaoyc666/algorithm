#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _113_path-sum-ii.py
Author       : miaoyc
Create date  : 2022/3/8 3:47 PM 
Description  : 路径总和 II
"""

"""
难度：中等

给你二叉树的根节点root和一个整数目标和targetSum，找出所有从根节点到叶子节点路径总和等于给定目标和的路径。
叶子节点是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]

提示：
树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.res = []
        self.tmp = []

    def pathSum(self, root, targetSum):
        """
        path sum
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.dfs(root, targetSum)
        return self.res

    def action(self, root, target):
        if root.val == target and not root.left and not root.right:
            a = copy.deepcopy(self.tmp)
            a.append(root.val)
            self.res.append(a)
        self.tmp.append(root.val)

    def dfs(self, root, target):
        if not root:
            return
        self.action(root, target)
        if root.left:
            self.dfs(root.left, target - root.val)
        if root.right:
            self.dfs(root.right, target - root.val)
        self.tmp.pop()
