#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _114_print-in-order.py
Author       : miaoyc
Create date  : 2020/6/22
Description  : 信号量
"""

from threading import Lock


class Foo(object):
    def __init__(self):
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.first_job_done.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.first_job_done:
            printSecond()
        self.second_job_done.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.second_job_done:
            printThird()
