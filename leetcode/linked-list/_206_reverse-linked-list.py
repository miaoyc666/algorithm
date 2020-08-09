#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _206_reverse-linked-list.py
Author       : miaoyc
Create date  : 2020/8/9 3:25 下午
Description  : 反转链表解法
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
