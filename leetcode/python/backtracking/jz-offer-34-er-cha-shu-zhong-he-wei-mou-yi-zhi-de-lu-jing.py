#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-34-er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing.py
Author       : miaoyc
Create date  : 2022/3/8 3:38 PM 
Description  : 二叉树中和为某一值的路径
"""

"""
难度：中等

与113 path-sum-ii题目重复

给你二叉树的根节点root和一个整数目标和targetSum，找出所有从根节点到叶子节点路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

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

