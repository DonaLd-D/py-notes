## 第二章 变量和简单数据类型

> ### 修改字符串的大小写的方法

  1. title() 将每个单词的首字母都改写为大写

  2. upper() 将字符串改为全部大写

  3. lower() 将字符串改为全部小写

> ### 使用制表符或换行符来添加空白

  1. \t 在字符串中添加制表符

  2. \n 在字符串中添加换行符

> ### 删除空白

  1. rstrip() 删除字符串末尾都空白

  2. lstrip() 剔除字符串开头都空白

  3. strip() 剔除字符串两边都空白

```
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language=' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
```

## 第三章 列表简介

> ### []表示列表，并用逗号分隔其中的元素，索引从0而不是1开始

> ### 修改、添加和删除元素

  1. lst.append(val)在列表尾部添加元素

  2. lst.insert(idx,val)在列表的任何位置添加新元素

  3. del lst[idx]->value 知道要删除元素在列表中位置，并删除

  4. lst.pop([idx])->value 删除并返回索引idx(默认为结尾)的元素，并接着使用它

  5. lst.remove(val)找到val在该列表的位置，并删除

> ### 组织列表

  1. lst.sort() 永久性地修改列表元素的排列顺序

  2. lst.reverse() 倒着打印列表

  3. len(c) 可快速获悉列表的长度
 
```
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'haojue')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.reverse()
print(cars)
print(len(cars))
```

## 第四章 操作列表

> ### for循环，遍历整个列表，对列表中的每个元素都执行相同的操作

> ### 创建数值列表

  1. range([start,]end[,step])生成系列数，或创建数字列表

  2. min(c) max(c) sum(c) 对数字列表执行简单的统计计算

  3. 列表解析 将for循环和创建新元素的代码合并成一行，并自动附加新元素

> ### 使用列表的一部分

  1. 切片 和range()同理，在到达第二个索引之前的元素后停止

  2. 遍历切片 如果要遍历列表的部分元素，可在for循环中使用切片

  3. 复制列表 根据既有列表创建全新的列表

> ### 元组(不可变的列表)

  1. 元组 元组看起来很像列表，但使用圆括号而非方括号来标识

  2. 遍历元组 用for循环来遍历

  3. 修改元组变量 虽然不能修改元组但元素，但可以给存储元组但变量赋值

```
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for players in players[0:3]:
    print(player.title())
```

## 第五章 if语句

> ### 条件测试

  1. == 相等运算符在两边的值相等时返回True,否则返回false

  2. != 判断两个值是否不等

  3. < >= <= > 数值比较

  4. and or 检查多个条件

  5. 布尔表达式 结果要么为True,要么为False

> ### if语句

  1. if-else结构 在条件测试通过时执行一个操作，在没有通过时执行另一个操作

  2. if-elif-else结构 依次检查每个条件测试，直到遇见通过了的条件测试

  3. elif代码块 表示多个条件语句

```
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")

age = 12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"Your admission cost is ${price}.")
```

## 第六章 字典

> ### 使用字典

  1. 访问字典中的值

  2. 添加(或创建)键值对

  3. 修改字典中的值

  4. 删除键值对(注：删除的键值对会永远消失。)

  5. 使用get()来访问值

> ### 遍历字典

  1. for 循环遍历所有键值对

  2. 遍历字典中对所有键值

```
alien_0={'color':'green','points';5}
print(alien_0['color'])

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.")

del alien_0['points']
print(alien_0)

alien_1={'color':'green','speed':'slow'}
point_value=alien_0.get('point','No point value assigned.')
print(point_value)

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print(f"key:{key}")
    print(f"value:{value}")
```
## 第七章 用户输入和while循环

> ### 函数input()的工作原理

  1. input()让程序暂停运行，等待用户输入一些文本

  2. int()获取数值输入

  3. 求模运算符%，它将两个数相除并返回余数

> ### 使用while循环

* for循环用于针对集合中的每个元素都执行一个代码块，而while循环则不断运行，直到指定的条件不满足为止。

```
height=input("how tall are you,in inches?")
height=int(height)
if height>=48:
    print("\nyou are tall enough to ride!")
else:
    print("\nyou will be able to ride when you are a little older.")

current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
```

## 第八章 函数

> ### 函数定义

* 函数是带有名字的代码块，用于完成具体的工作，使用关键词def来定义。

> ### 函数调用

* 需要在程序中多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该任务的函数，让python运行其中的代码即可。

```
def greet_user(user_name):
    print(f"hello!{user_name.title()}")
greet_user("nana")
```

## 第九章 类
> ### 方法__init__()


* 方法__init__()是一个特殊方法，每当你根据Dog类创建新实例时，python
* 都会自动运行它，在这个方法的名称中，开头和末尾各有两个下划线，这是一种
* 约定，旨在避免python默认方法与普通方法发生名称冲突。务必确保__init__()
* 的两边都有两个下划线，否则当你使用类来创建实例时，将不会自动调用这个方法，
* 进而引发难以发现的错误。

```
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name}is now sitting.")
    def roll_over(self):
        print(f"{self.name}rolled over!")

my_dog=Dog('willie',6)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
```


