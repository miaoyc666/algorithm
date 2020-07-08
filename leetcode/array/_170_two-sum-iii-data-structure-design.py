#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _170_two-sum-iii-data-structure-design.py
Author       : miaoyc
Create date  : 2020/6/21
Description  :
"""

"""
设计并实现一个 TwoSum 的类，使该类需要支持 add 和 find 的操作。

add 操作 -  对内部数据结构增加一个数。
find 操作 - 寻找内部数据结构中是否存在一对整数，使得两数之和与给定的数相等。

示例 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
示例 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

import collections


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.data[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        numbers = self.data.keys()
        for i in numbers:
            if value == i * 2 and self.data[i] >= 2:
                return True
            if value - i in self.data:
                if value - i != i:
                    return True
                if value - i == i and self.data[i] >= 2:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
