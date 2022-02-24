# 解题训练

###项目说明  
- just to keep my mind sharp!
- 代码版本包含Python2/3、Golang和Rust，不同编程语言代码结构最顶层进行区分，Python2/3不进行区分
- 所有代码均为网站提交通过版本代码 
- 刷题顺序为先刷简单题，目的是地毯式消灭简单题目，达到笔随心动，流畅搬砖
- 类型题解题模板单独按类型整理：[解题模板](./doc/template/template.md) 

###当前进度  
- leetcode algorithms: 119（重复题目：6）
- hihocoder: 4
- leetcode database: 1

###刷题圣经  
二叉树篇：  
1. 中序遍历二叉搜索树等于遍历有序数组； 

数组：  
1. 双指针要分别更新首尾指针，可避免处理边界问题；  

滑动窗口：  
1. 滑动窗口题目首先要确定窗口的长度，其次是确定左右游标的边界条件；

###随笔记录  
1. 在刷了13道dfs的题目后，对二叉树问题处理的时候，代码写的明显更顺畅了；21.7.4  
2. 在刷到17道dfs的题目后，处理二叉树问题已经不需要看题解和评论了，从自己写过的代码就可以找到思路并copy代码；21.7.7  
3. Python3的set结构在数据量少的情况下有序是由解释器实现决定的，只能算是凑巧而已；21.8.1  
4. rust递减生成数组的时候竟然是先递增生成再反转，就是这个语句(0..n).rev()，来个n..0不是更好？；21.9.6  
5. 当n为奇数时，n与1亦或得到的是n - 1，n ^ 1 = n - 1。当n为偶数时，n与1亦或得到的是n + 1，n ^ 1 = n + 1；22.2.15

###代码技巧
##### Python
1. list*2相当于list.extend(list); 21.7.14
2. Py2中，/表示地板除，即舍弃小数部分下取整。在Py3中，/表示除法，//表示地板除；21.8.24 
3. 字符串内置函数isalnum()，用于检测字符串是否由字母和数字组成，这个内置函数堪称黑科技；21.9.30  
4. collections.Counter()可以选择字符串作为传参来生成一个针对每个字符的计数器；21.11.14 
5. Py3初始化指定长度为n的数组a=[0] * n；22.1.3
6. nums[:]的作用是深拷贝了数组变量nums；22.1.20
7. collections.Counter()最常用的用法时传入list得到list中元素计数的dict；22.2.7
8. collections.Counter()可传入迭代器作为参数；22.2.13
9. 与技巧3同源，字符串内置函数isalpha()，用于检测字符串是否只由字母组成，技巧3和技巧9可以让开发者免除判断ascii码的烦恼；22.2.23

##### Rust
1. 使用vec!宏创建有初始值的动态树组；21.11.22

