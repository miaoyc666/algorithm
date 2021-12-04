# File name    :  175_combine-two-tables.sql
# Author       : miaoyc
# Create date  : 2021/12/4 10:46 下午
# Description  : 组合两个表

/*
表1: Person
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键

表2: Address
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键

编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供person 的以下信息：

FirstName, LastName, City, State
*/

select a.FirstName, a.LastName, b.City, b.State from Person a left join Address b on a.PersonId = b.PersonId