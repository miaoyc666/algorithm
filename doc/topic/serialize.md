# 序列化问题

##### 序列化和反序列化二叉搜索树
- 题目：[serialize-and-deserialize-bst](../../leetcode/python/serialize/_449_serialize-and-deserialize-bst.py)
- 难度：中等
- 解题思路：  
  1.二叉搜索树的特点为左孩子节点比父节点小，右孩子节点比父节点大，可以利用该特性进行反序列化；  
  2.序列化时使用后续遍历，可以保证root节点在序列化列表的末尾；  
  3.反序列化时，每次递归遍历序列化数据中的一条数据。  

##### 二叉树的序列化与反序列化
- 题目：[serialize-and-deserialize-binary-tree](../../leetcode/python/serialize/_297_serialize-and-deserialize-binary-tree.py)
- 难度：困难
- 解题思路：bfs层序遍历进行序列化，空节点用特殊字符进行填充，反序列化时使用层序遍历进行树的构建
