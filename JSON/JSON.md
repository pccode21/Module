JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。
==========================================================
1.JSON的2种结构形式:
----------------------------
（1）键值对形式:<br>
  “名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。<br>
  这种结构的JSON数据规则是：对象是一个无序的“‘名称/值’对”集合。一个对象以 {左括号 开始， }右括号 结束。每个“名称”后跟一个 :冒号 ；“‘名称/值’ 对”之间使用 ,逗号 分隔。<br>
（2）数组形式：<br>
  值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。<br>
  数组是值（value）的有序集合。一个数组以 [左中括号 开始， ]右中括号 结束。值之间使用 ,逗号 分隔。<br>

2.JSON的6种数据类型:
----------------------------
  上面两种JSON形式内部都是包含value的，那JSON的value到底有哪些类型，而且上期我们说JSON其实就是从Js数据格式中提取了一个子集，那具体有哪几种数据类型呢？<br>
  string：字符串，必须要用双引号引起来。<br>
  number：数值，与JavaScript的number一致，整数（不使用小数点或指数计数法）最多为 15 位。小数的最大位数是 17。<br>
  object：JavaScript的对象形式，{ key:value }表示方式，可嵌套。<br>
  array：数组，JavaScript的Array表示方式[ value ]，可嵌套。<br>
  true/false：布尔类型，JavaScript的boolean类型。<br>
  null：空值，JavaScript的null。<br>
JSON官方文档：http://www.json.org/json-zh.html <br>
