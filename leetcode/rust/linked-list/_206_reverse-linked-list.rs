/*
File name    : _206_reverse-linked-list.rs
Author       : miaoyc
Create date  : 2021/11/2 12:33 上午
Description  : 反转链表
*/

/*
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
*/

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        /*
            解题思路：
            定义两个节点，prev代表前一个节点，curr代表当前的节点。初始将prev节点设置为空， curr节点设置为头结点head。
            遍历链表，将curr节点的next指针改为指向prev节点，再分别将prev和curr节点向后移动一个节点。
            遍历完成后，curr节点为空，prev节点就是新的头结点。
        */
       let mut prev = None;
       let mut curr = head;
       // 使用while let简化模式匹配处理
       while let Some(mut curr_node) = curr.take() {
           // 保存当前节点的下一个节点
           let next_temp = curr_node.next.take();   // 使用Option的take方法取值
           // 将当前节点指向prev
           curr_node.next = prev.take();
           // prev和curr分别往后移动一个节点，即把当前节点curr_node赋值给prev，把之前保存的当前节点的下一个节点next_temp赋值给curr
           prev = Some(curr_node);
           curr = next_temp;
       }
       return prev;
    }
}
