#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _2525_reward-top-k-students.py
Author       : miaoyc
Create date  : 2023/10/11 21:14
Description  : 
"""


class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        words = {}
        for w in positive_feedback:
            words[w] = 3
        for w in negative_feedback:
            words[w] = -1
        A = []
        for s, i in zip(report, student_id):
            score = sum(words.get(w, 0)for w in s.split())
            A.append([-score, i])
        A.sort()
        return [i for v,i in A[:k]]
