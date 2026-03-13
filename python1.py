'''列表的学习'''#可修改
a = [1,2,3]
print(a[1:3:1])#切片操作[其实索引：结束索引：步长]
a.append(1)#增加一个元素
a.extend([1,2,3])#将列表中的元素拆分后添加
a.insert(1, 5)#在指定位置插入元素(位置, 元素)
b = a.index(2)#查找元素2的第一次出现的索引
c = a.count(1)#统计元素出现次数
a.remove(1)#移除第一个匹配的元素
a.reverse()#将列表中的元素反转
print(a)
a.sort()#对列表进行(从大到小)排序
print(a)
a.sort(reverse=True)#对列表进行(从小到大)排序
print(a)
print(f"元素2的索引是: {b}")
print(f"元素1出现的次数是: {c}")
'''元组的学习'''#不可修改
t = (1, 2, 3)
print(t)
'''字典的学习'''#可修改
d = {"name": "Alice", "age": 25}  #冒号前的是键，冒号后的是值，包值赋给键
d["age"] = 10#修改键的值
print(d) 
print(d.get("name")) #只能找到存在的键


