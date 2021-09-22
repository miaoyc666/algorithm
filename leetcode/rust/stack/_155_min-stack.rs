/*
File name    : _155_min-stack.rs
Author       : miaoyc
Create date  : 2021/9/8 12:05 上午
Description  : 最小栈
*/

/*

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop()—— 删除栈顶的元素。
top()—— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
*/

struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>
}

/*
1.算法原理
使用两个栈，一个数据栈stack用于存放正常入栈和出栈的数据，另一个辅助站min_stack用于存取stack中的最小值。
min_stack等价于遍历stack中所有的元，把升序的数据全部删除掉，留下一个从栈底到栈顶降序的栈。

2.算法流程
push方法：判断push的数据是否小于等于min_stack的栈顶元素，如果是，则min_stack也push该数值;
pop方法：判断pop的数据是否等于min_stack栈顶元素，如果是则让min_stack也同步pop栈顶元素;
get_min方法：返回min_stack的栈顶元素。
*/

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new()
        }
    }

    fn push(&self, val: i32) {

    }

    fn pop(&self) {

    }

    fn top(&self) -> i32 {

    }

    fn get_min(&self) -> i32 {

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
