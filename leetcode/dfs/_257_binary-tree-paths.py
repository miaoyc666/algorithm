#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _257_binary-tree-paths.py
Author       : miaoyc
Create date  : 2021/7/2 11:21 下午
Description  : 二叉树的所有路径
"""

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self):
        self.stack = []
        self.roads = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.dfs(root)
        return self.roads

    def dfs(self, root):
        if not root:
            return False

        self.stack.append("{0}".format(root.val))

        if not root.left and not root.right:
            self.roads.append("->".join(self.stack))
            self.stack.pop(-1)

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left or right:
            self.stack.pop(-1)

        return True


if __name__ == "__main__":
    p = TreeNode()
    pl = TreeNode()
    pr = TreeNode()
    root = TreeNode()

    p.val = 5
    p.left = None
    p.right = None

    pl.val = 2
    pl.left = None
    pl.right = p

    pr.val = 3
    pr.left = None
    pr.right = None

    root.val = 1
    root.left = pl
    root.right = pr

    print Solution().binaryTreePaths(root)
