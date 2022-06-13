#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _1022_sum-of-root-to-leaf-binary-numbers.py
Author       : miaoyc
Create date  : 2022/5/30 20:54 
Description  : 从根到叶的二进制数之和
"""

"""
难度：简单

给出一棵二叉树，其上每个结点的值都是0或1。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
例如，如果路径为0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数01101，也就是13。
对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
返回这些数字之和。题目数据保证答案是一个 32 位 整数。

示例 1：
输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

示例 2：
输入：root = [0]
输出：0

提示：
树中的节点数在[1, 1000]范围内
Node.val仅为 0 或 1
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preorder(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    nums.append(int(path, 2))         # 把路径加入到答案中
                else:
                    # 当前节点不是叶子节点，继续递归遍历
                    preorder(root.left, path)
                    preorder(root.right, path)
        nums = []
        preorder(root, '')
        return sum(nums)


