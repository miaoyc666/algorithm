/*
File name    : _66_plus-one.rs
Author       : miaoyc
Create date  : 2021/9/6 12:08 上午
Description  : 加一
*/

/*
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
*/


/*
解题思路：
反向遍历数组，依次取元素加一，可能出现以下三种情况：
1.末位数据不是9，末位加一，前面所有数字保持不变；
2.末位数据是9，但非全部数据都是9，末位数字加一后进位，循环向前走，依次类推；
3.所有数字都是9，数组长度加1，第一位是1，其余位数皆为0
*/


impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut length = digits.len();
        for i in (0..length).rev() {
            if digits[i] < 9 {
                // 数字不为9的情况
                digits[i] += 1;
                return digits;
            } else {
                // 数字为9的情况
                digits[i] = 0;
                if i >= 1 {
                    continue
                } else {
                    // 全部数字为9的分支情况
                    let mut res = vec![0; digits.len() + 1];
                    res[0] = 1;
                    return res;
                }
            }
        }
        return digits;
    }
}
