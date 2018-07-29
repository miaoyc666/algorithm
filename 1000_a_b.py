#!/usr/bin/ython
# encoding:utf-8

"""
hihocoder题目描述
时间限制:1000ms
单点时限:1000ms
内存限制:256MB
描述
求两个整数A+B的和

输入
输入包含多组数据。
每组数据包含两个整数A(1 ≤ A ≤ 100)和B(1 ≤ B ≤ 100)。

输出
对于每组数据输出A+B的和。

样例输入
1 2
3 4
样例输出
3
7
"""

"""
hihocoder题解
while True:
    try:
        (x, y) = (int(x) for x in raw_input().split())
        print x + y
    except EOFError:
        break
"""


def a_b(num_lst):
    try:
        return [nums[0] + nums[1] for nums in num_lst]
    except Exception as e:
        print e


if __name__ == "__main__":
    input_v = [[1, 2], [3, 4]]
    print '\n'.join([str(x) for x in a_b(input_v)])
