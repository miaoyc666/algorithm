#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-09-yong-liang-ge-zhan-shi-xian-dui-lie-lcof.py
Author       : miaoyc
Create date  : 2022/1/1 11:13 下午
Description  : 用两个栈实现队列
"""

"""
难度：简单

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对appendTail、deleteHead 进行10000次调用
"""

"""
解题思路：
使用两个栈，一个栈stack1用来push数据，另一个栈stack2用于存放stack1出栈后的数据，stack2的数据与stack1的数据为逆序的，以此实现stack2的pop操作相当于与stack1的pop(0)，实现先进先出
"""


class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            if not self.stack1:
                return -1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
