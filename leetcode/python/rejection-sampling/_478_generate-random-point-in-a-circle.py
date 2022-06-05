#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : _478_generate-random-point-in-a-circle.py
Author       : miaoyc
Create date  : 2022/6/5 23:29
Description  : 在圆内随机生成点
"""

"""
难度：中等

给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。

实现Solution类:
Solution(double radius, double x_center, double y_center)用圆的半径radius和圆心的位置 (x_center, y_center) 初始化对象
randPoint()返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。


示例 1：
输入: 
["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

解释:
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]

提示：
0 <radius <= 108
-107<= x_center, y_center <= 107
randPoint 最多被调用3 * 104次
"""

import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.xc + x, self.yc + y]
