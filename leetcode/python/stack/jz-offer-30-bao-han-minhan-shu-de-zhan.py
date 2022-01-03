#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-30-bao-han-minhan-shu-de-zhan.py
Author       : miaoyc
Create date  : 2022/1/2 11:05 下午
Description  : 最小栈
"""

"""
难度：简单

与155 min-stack题目重复
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
