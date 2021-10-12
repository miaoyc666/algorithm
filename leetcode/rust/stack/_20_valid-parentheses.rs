/*
File name    : _20_valid-parentheses.rs
Author       : miaoyc
Create date  : 2021/9/25 11:49 下午
Description  : 
*/

/*
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
*/

/*
以下为python实现，本打算用rust来按照此思路实现代码，但是对字典操作不是很熟悉
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1

use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut dic = HashMap::new();
        let mut stack =  Vec::new();
        stack.push('?');
        for c in 0..s.chars() {
            if dic.contains_key(&c) {

            } else {
                x = stack.pop()

            }
            if c in dic{}

            match dic.get(&c) {
                stack.push(c),

                _ => println!("Don't have Daniel's number."),
            }


        }
    }
}
*/

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        // 判断是否为空字符串，空字符串视为有效字符串
        if chars.len() == 0 {
            return true;
        }
        let mut stack: Vec<char> = Vec::new();
        for i in 0..chars.len() {
            if chars[i] == '(' {        // 如果字符是左小括号，将右小括号入栈
                stack.push(')');
            } else if chars[i] == '[' { // 如果字符是左中括号，将右中括号入栈
                stack.push(']');
            } else if chars[i] == '{' { // 如果字符是左大括号，将右大括号入栈
                stack.push('}');
            } else if stack.is_empty() || chars[i] != stack.pop().unwrap() {    // 栈为空或字符与栈顶元素不相同时，为无效字符
                return false;
            }
        }
        // 匹配结束，栈为空代表是有效字符串，否则是无效字符串
        return stack.is_empty();
    }
}

