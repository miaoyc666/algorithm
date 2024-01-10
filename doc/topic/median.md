# 中位数问题

### 最小操作次数使数组元素相等
- 题目：[minimum-moves-to-equal-array-elements](../../leetcode/python/math/_453_minimum-moves-to-equal-array-elements.py)
- 难度：简单
- 解题思路：n-1个数同时+1，相当于每次有1个数自身-1，因为只能做减法，所以数组最后的数只能是最小值。因此，每个元素减去最小值求其和就是答案

### 最小操作次数使数组元素相等II
- 题目：[minimum-moves-to-equal-array-elements-ii](../../leetcode/python/math/_462_minimum-moves-to-equal-array-elements-ii.py)
- 难度：中等
- 解题思路：解题关键是找到中位数，找到中位数后，迭代所有差值即拿到最终结果

### 最佳的碰头地点
- 题目：[best-meeting-point](../../leetcode/python/math/_296_best-meeting-point.py)
- 难度：困难
- 解题思路：曼哈顿距离在x和y两个方向上是独立的，只要找到所有人x坐标和y坐标的中位数即可，这个中位数的坐标就是最优结果。
