#coding=utf-8
#变量和简单数据类型
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language=' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#列表简介
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

#操作列表
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for players in players[0:3]:
    print(player.title())

#if语句
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

#字典
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

#用户输入和while循环
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

#函数
def greet_user(user_name):
    print(f"hello!{user_name.title()}")
greet_user("nana")

#类
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

