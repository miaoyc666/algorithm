#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test2.py
Author       : miaoyc
Create date  : 2021/12/25 7:01 下午
Description  : 
"""

"""
python编程，有如下规则将一串数字编码成一串字母，1-＞a，2-＞b，...，26-＞z，例如123可以编码成abc，lc，aw共3种结果，给定任意一串数字，返回编码结果的数量
注：数字中没有0
"""

# 暂定所有字符均不为0
# 问题的核心解法为依据数字字符串构建二叉树，树的节点为小于26, 左子树为一位数据，右子树为两位数字
# 遍历每一条路径可以得到完整的数字，路径数目即为编码结果的数量


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_two_nums(s, index):
    if index < 0 or index > len(s) - 1:
        return 0
    else:
        return s[index: index+2]


def dfs(root, value, s, index):
    # 退出条件为遍历结束
    if index < 0 or index > len(s) - 1:
        return None

    root.val = value

    # 将剩余数字走左子树遍历逻辑
    root.left =
    dfs(root.left, s[index+1:index+2], s, index+1)

    # 判断右子树是否需要遍历
    two_nums = get_two_nums(s, index)
    if 10 < int(two_nums) < 26:
        dfs(root.right, s[index+1:index+3], s, index+2)


class Solution:

    def __init__(self):
        self.count = 0

    def is_node(self, root):
        if not root.left and not root.right:
            self.count += 1
            return True
        else:
            return False

    def inorder(self, root):
        # 退出条件，此处root节点不存在仅为举例
        if not root:
            return
        self.inorder(self, root.left)
        self.is_node(root)
        self.inorder(self, root.right)

    def get_count(self):
        return self.count


if __name__ == "__main__":
    p = TreeNode()
    p.val = "root"
    p.left = None
    p.right = None
    a = 123
    a_str = str(a)
    dfs(p, "root", a_str, 0)

    solution = Solution()
    solution.inorder(p)
    print(solution.get_count())



