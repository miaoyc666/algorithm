#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _112_path-sum.py
Author       : miaoyc
Create date  : 2021/6/27 11:51 下午
Description  : 路径总和
"""

"""
难度：简单 

给你二叉树的根节节root和一个表示目标和的整数targetSum，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和targetSum。
叶子节点是指没有子节点的节点。

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
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
解题思路：
前序遍历所有节点即可
"""


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def preorder(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)                # 把路径加入到答案中
                else:
                    path += '->'                      # 当前节点不是叶子节点，继续递归遍历
                    preorder(root.left, path)
                    preorder(root.right, path)
        paths = []
        preorder(root, '')
        return paths
