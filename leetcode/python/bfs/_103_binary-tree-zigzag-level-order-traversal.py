#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _103_binary-tree-zigzag-level-order-traversal.py
Author       : miaoyc
Create date  : 2023/4/19 23:32
Description  : 二叉树的锯齿形层序遍历
"""

"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100
"""