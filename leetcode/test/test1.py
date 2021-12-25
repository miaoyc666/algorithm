#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : test1.py
Author       : miaoyc
Create date  : 2021/12/25 5:06 下午
Description  : 
"""

"""
python编程，给出任意一个二维字符数组和一个字符串，判断字符串是否在数组中出现，字符串由相邻单元格（上下左右都算相邻）的字母连接而成。
例如：
字符数组=
[
  ["XYZE"],
  ["SFZS"],
  ["XDEE"]
]

"XDEZZ"返回True,
"SFZF"返回True,
"XYZX"返回False.
"""


def find_next_char(target, index):
    if index < 0 or index > len(target) - 1:
        return None
    return target[index]


def find_string(matrix, target):
    # 1.边界条件判断
    if not matrix:
        return False

    # 2.首字符匹配
    head_list = [x[0] for x in matrix]
    if target[0] not in head_list:
        return False

    # 3.从0，0坐标开始dfs遍历
    # i, j作为坐标变量
    for ii in range(0, len(matrix)):
        # print("next target str", target[0])
        # print(target)
        r = dfs(matrix, target, target[0], 0, ii, 0)
        if r:
            return True
    return False


def dfs(matrix, target, target_str, target_index, i, j):
    """
    :param matrix:
    :param target:
    :param target_str:
    :param target_index:
    :param i: 纵坐标
    :param j: 横坐标
    :return:
    """
    # 找到target在matrix中，并且target_index = len(target) - 1, 即最后一个字符也在matrix中找到, 此时可以遍历结束
    if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1:
        return False
    # print("---->", matrix[i][j], target_str)
    if matrix[i][j] == target_str:
        if len(target) - 1 == target_index:
            return True
        # print("next target str", target_str)
        target_index += 1
        target_str = find_next_char(target, target_index)
        if not target_str:
            return False
        # print("next target str", target_str)
        right = dfs(matrix, target, target_str, target_index, i, j + 1)
        # print("right", matrix[i][j+1], target_str, right)
        left = dfs(matrix, target, target_str, target_index, i, j - 1)
        # print("left", matrix[i][j-1], target_str, left)
        down = dfs(matrix, target, target_str, target_index, i + 1, j)
        # print("down", matrix[i+1][j], target_str)
        up = dfs(matrix, target, target_str, target_index, i - 1, j)
        # print("up", matrix[i-1][j], target_str, up)
        # print(right, left, up, down)
        if right or left or down or up:
            return True
    else:
        return False


if __name__ == "__main__":
    a = [
        ["XYZE"],
        ["SFZS"],
        ["XDEE"]
    ]
    i_ = "XDEZZ"
    j_ = "SFZF"
    k_ = "XYZX"

    matrix_ = [x[0] for x in a]
    # for i in matrix_:
    #     print(i)
    # print(i_)
    print(find_string(matrix_, i_))
    print(find_string(matrix_, j_))
    print(find_string(matrix_, k_))

