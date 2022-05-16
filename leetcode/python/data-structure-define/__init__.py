#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : __init__.py
Author       : miaoyc
Create date  : 2022/5/16 11:47 
Description  : 数据结构定义
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
