#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _170_two-sum-iii-data-structure-design.py
Author       : miaoyc1989@hotmail.com
Create date  : 2020/6/21
Description  : 
"""


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
        numnbers = self.data.keys()
        for i in numnbers:
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
