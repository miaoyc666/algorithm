#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer2-24-fan-zhuan-lian-biao.py
Author       : miaoyc
Create date  : 2022/1/3 9:42 下午
Description  : 反转链表
"""

"""
难度：简单

与206 reverse-linked-list题目重复
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        pre, cur = None, head
        while cur:
            # 当前指针的后指针赋值给临时变量
            temp = cur.next
            # 反转当前指针与前指针
            cur.next = pre
            pre = cur
            # 连接链表
            cur = temp
        return pre
