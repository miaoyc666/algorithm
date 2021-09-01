#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _100_same_tree.py
Author       : miaoyc
Create date  : 2021/6/22 1:22 上午
Description  : 相同的树
"""

"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：

输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：

输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：

输入：p = [1,2,1], q = [1,1,2]
输出：false

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            return not q
        if p and not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    p = TreeNode()
    q = TreeNode()
    pl = TreeNode()
    pr = TreeNode()
    ql = TreeNode()
    qr = TreeNode()

    pl.val = 2
    pl.left = None
    pl.right = None

    pr.val = 1
    pr.left = None
    pr.right = None

    p.val = 1
    p.left = pl
    p.right = pr

    ql.val = 1
    ql.left = None
    ql.right = None

    qr.val = 2
    qr.left = None
    qr.right = None

    q.val = 1
    q.left = ql
    q.right = qr

    print Solution().isSameTree(p, q)
