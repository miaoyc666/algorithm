#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : jz-offer-02-cong-wei-dao-tou-da-yin-lian-biao.py
Author       : miaoyc
Create date  : 2022/1/3 9:35 下午
Description  : 
"""

"""
难度：简单

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
"""


from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self):
        self.length = 0
        self.nums = []

    def reversePrint(self, head: ListNode) -> List[int]:
        tmp = head
        while tmp:
            self.length += 1
            tmp = tmp.next
        self.nums = [0] * self.length
        while head:
            self.nums[self.length-1] = head.val
            self.length -= 1
            head = head.next
        return self.nums
