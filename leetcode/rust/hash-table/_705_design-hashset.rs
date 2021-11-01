/*
File name    : _705_design-hashset.rs
Author       : miaoyc
Create date  : 2021/11/1 12:51 下午
Description  : 设计哈希集合
*/

/*
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
实现 MyHashSet 类：
void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例：
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）

提示：
0 <= key <= 106
最多调用 104 次 add、remove 和 contains 。
*/

/*
python 实现，该实现在leetcode提交执行会超时，python还是慢。
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class HashNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.base = 769213
        self.base = 1000000
        self.data = [HashNode(0) for _ in range(self.base)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        head = self.data[key % self.base]
        cur = HashNode(key)
        cur.next = head.next
        head.next = cur

    def remove(self, key: int) -> None:
        head = self.data[key % self.base]
        pre = head
        while head.next:
            cur = head.next
            if cur.val == key:
                pre.next = cur.next
                break
            pre = cur

    def contains(self, key: int) -> bool:
        head = self.data[key % self.base]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False
*/

struct GrayscaleMap {
    pixels: Vec<u8>;
    size: (usize, usize);
}

/*
此处理想情况应该是支持模板
TODO: 看一下Rust hashset的实现
参考文章：https://zhuanlan.zhihu.com/p/341626700
*/

struct HashNode {
    val: i32;
    next:

}

struct MyHashSet {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    fn new() -> Self {

    }

    fn add(&self, key: i32) {

    }

    fn remove(&self, key: i32) {

    }

    fn contains(&self, key: i32) -> bool {

    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
