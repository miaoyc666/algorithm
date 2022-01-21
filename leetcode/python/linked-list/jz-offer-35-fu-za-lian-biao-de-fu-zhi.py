#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-35-fu-za-lian-biao-de-fu-zhi.py
Author       : miaoyc
Create date  : 2022/1/3 10:35 下午
Description  : 复杂链表的复制
"""

"""
难度：中等
与138 copy-list-with-random-pointer题目重复
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        buf = dict()
        cur = head
        while cur:
            buf[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            buf[cur].next = buf.get(cur.next)
            buf[cur].random = buf.get(cur.random)
            cur = cur.next
        return buf[head]
