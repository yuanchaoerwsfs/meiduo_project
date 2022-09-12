import this

name = 'AdA lover your!'
print(name.title())  # 输出字母首字母全部大写
print(name.lower())  # 输出字母全部为小写
print(name.upper())  # 输出字母全部为大写

print('language:\tHello\n word \n!')  # \n 换行  \t空格
test = '    language：Hello word !     '
print(test)
print('=' * 50)
print(test.rstrip())  # rstrip()  会将原有数据末尾空格删除，并可保存到新的变量中
print(test.lstrip())  # lstrip()  会将原有数据首部空格删除，并可保存到新的变量中
print(test.strip())  # strip()  会将原有数据首部和末尾空格删除，并可保存到新的变量中

name_f = 'albert einstein'
f_say = 'once said,'
A = '"a '
text = 'preson who never made a mistake never tried anything new"'
famous_person = 'albert einstein'
message = f_say.lower() + A.upper() + text.lower()
print(name_f.title() + ' ' + f_say.lower() + A.upper() + text.lower())
print(famous_person.title() + ' ' + message)

age = 23
print('my age is' + ' ' + str(age))

print(3 / 2)
print(3.0 / 2)

# 列表
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print(bicycle[0].title())  # 使用title()必须在列后加元素索引‘[0---。。。。]’
print(bicycle[1].upper())
print(bicycle[-1].lower())

friend_name = ['sunqw', 'baizt', 'wangxt', 'lijian', 'liucg']  # 列表
print(friend_name)
friend_name[0] = 'sunquanwei'  # 修改指定数据
friend_name.append('liu jia')  # 尾部添加数据
for i in friend_name:
    print('my friend name is:' + i.title())

print('==' * 50)

arr_insert = []  # 空列表不能修改数据方法添加数据
arr_insert.append('liu jia')  # 尾端添加智能添加一个数据
arr_insert.insert(0, 'sun quan wei')  # 添加数据,只能指定位置添加
print(arr_insert[0].title())
print(arr_insert[1].upper())
arr_pop = arr_insert.pop()
print(arr_pop.title())

arr_test = ['sun quan wei', 'sun da fu', 'hei mei mei', 'liu da sha']

arr_test.pop(2)  # pop()  括号内可填入删除参数
print(arr_test)
arr_test.remove('sun quan wei')  # remove 根据传入参数值删除数据
print(arr_test)

# 练习
arr_test1 = ['sun quan wei', 'sun da fu', 'hei mei mei', 'liu da sha']
quest = arr_test1.pop()
print('因为' + quest + '有时无法参加聚餐邀请')
quest1 = arr_test1.pop()
print(quest1 + '可以接受邀请')
test = ['liu liu', 'qi qi ', 'fei fei', 'xing xing ']
for i in test:
    arr_test1.append(i)
arr_test1.insert(3, 'xi xi')
print(arr_test1)
# =========================================以下两步临时排序不生效
sorted(arr_test1)
print(arr_test1)
# ===================================================
print(sorted(arr_test1))  # 只有这样写临时排序才生效
print("===" * 50)
arr_test1.sort()  # 永久排序,直接改变列表数据按照字母顺序排序
print(arr_test1)
# =======================================================永久倒叙排列
arr_test1.reverse()
print(arr_test1)
# ========================================================数据长度测量函数,len函数返回长度可用变量接收
print(len(arr_test1))
# ==================================================
for values in range(1, 5):  # 不打印5
    print(values)
test_range = list(range(1, 5))  # list 将range转化为列表存储
print(test_range)

square = []
for values in range(1, 10):
    square1 = values ** 2  # '**2' 表示平方 以此类推
    square.append(square1)
print(square)
# ====================================完成最大值、最小值、求和计算
sq_min = min(square)
sq_max = max(square)
sq_sum = sum(square)
print('min=' + str(sq_min), 'max=' + str(sq_max), 'sum=' + str(sq_sum))

# ======================================
# 要使用这种语法，首先指定一个描述性的列表名，如squares ；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为
# value**2 ，它计算平方值。接下来，编写一个for 循环，用于给表达式提供值，再加上右方括号。在这个示例中，for 循环为for value in range(1,11) ，它将值
# 1~10提供给表达式value**2 。请注意，这里的for 语句末尾没有冒号。
square_test = [value ** 2 for value in range(1, 11)]
print(square_test)
# ==========================================练习
for i in range(1, 21):
    print(i)
list_test = list(range(1, 11))
for i in list_test:
    print(i)
list_min = min(list_test)
print(list_min)
list_max = max(list_test)
print(list_max)
list_sum = sum(list_test)
print(list_sum)

list_j = list(range(1, 20))
for i in list_j:
    if i % 2 != 0:
        print(i)
list_test1 = list(range(3, 30))
for i in list_test1:
    if i % 3 == 0:
        print(i)
list_test2 = list(range(1, 11))
for i in list_test2:
    temp = i ** 3
    print(str(i) + '的三次方是：' + str(temp))
# 列表解析
list_test3 = [value ** 3 for value in range(1, 11)]
print(list_test3)
# ==========================================复制切片
list_test4 = ['dai dai', 'xi xi', 'xiang xiang ', 'miao miao ']
list_test5 = list_test4[:]
list_test6 = list_test5
print(list_test5)
print(list_test6)
# ============================================ 元组不能修改删除元素，可以给元素赋值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

alien_color = 'green'
if alien_color == 'green':
    print('玩家获得5点经验值')
elif alien_color == 'red':
    print('玩家获得10点经验值')
elif alien_color == 'yellow':
    print('玩家活得15点经验值')
else:
    print('输入有误')
# =====================================================
A = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
B = ['mushrooms', 'french fries', 'extra cheese']
print(A)
for i in B:
    if i in A:
        print('B的' + i + '在A中存在')
    else:
        print('B的' + i + '在A中不存在')

# ===========================================================字典
sun = {}
sun['age'] = 25
sun['name'] = 'sun'
print(sun)
print(sun['name'])
# ============================================================遍历字典
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print('\nKey:' + key)
    print('values:' + value)
for k in user_0.keys():
    print('\nKey:' + k)
for v in user_0.values():
    print('\nvalue:' + v)

for name in sorted(user_0.keys()):  # 将字典排序，排序后进行遍历
    print(name.title())

print('==' * 50)

alien_00 = {'color': 'green', 'points': 5}
alien_01 = {'color': 'yellow', 'points': 10}
alien_02 = {'color': 'red', 'points': 15}
aliens = [alien_00, alien_01, alien_02]
print(aliens)
print('==' * 50)
active = True
# while active:
#     message = input('请输入')
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

print('==' * 50)
# =============================================列表移动
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    A = unconfirmed_users.pop()
    confirmed_users.append(A)
    print(confirmed_users)

sandwich_orders = ['hong shao niu rou', 'ji tui bao', 'hai xian lu zhan dui', 'ya ya ou', '五香烟熏牛肉', '五香烟熏牛肉', '五香烟熏牛肉']
finished_sandwich = []
for i in sandwich_orders:
    finished_sandwich.append(i)
    print(i)
print(finished_sandwich)

print('本店五香烟熏牛肉已经卖完')
active = True
while '五香烟熏牛肉' in sandwich_orders:
    sandwich_orders.remove('五香烟熏牛肉')
print(sandwich_orders)

dictionaries_city = {}


def city_country(city, state):
    dictionaries_city = {'city': city, 'state': state}
    return dictionaries_city


city_country('TianJin', 'China')
city_country('BeiJing', 'China')
city_country('XIAn', 'China')
print(dictionaries_city)

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\n The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print('==' * 50)
print(unprinted_designs)


def print_models(unprinted_designs, completed_models):
    """
      模拟打印每个设计，直到没有未打印的设计为止
      打印每个设计后，都将其移到列表completed_models中
      """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)

print('==' * 50)


def show_magicians(magicians):
    print(magicians)


magicians = ['iphone case', 'robot pendant', 'dodecahedron']


def make_great(magicians):
    temp = []
    index = 0
    for i in magicians:
        t = 'the Great ' + i
        magicians[index] = t
        temp.append(t)
        index = index + 1
    return temp


# make_great(magicians)
# print(magicians)
temp = make_great(magicians[:])  # 此实参表示不能修改列表内容
print(magicians)
print(temp)


def make_pizza(make, *toppings):  # 任意实参位置必须写在最后面
    print('make:' + make)
    for topping in toppings:
        print(topping)


make = 'China'
make_pizza(make, 'green peppers', 'extra topping', 'mushrooms')
make_pizza(make, 'green peppers111', 'extra topping111', 'mushrooms111')
make_pizza(make, 'green peppers222', 'extra topping222', 'mushrooms222')


def build_profile(first, last, **user_info):  # 传输字典形参可使用**
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)


def inpit_add():
    try:
        print('请输入两个数字')
        A = input()
        B = input()
        C = int(A) + int(B)
    except ValueError:
        print('输入数据有误')
    else:
        print(C)


inpit_add()

name=input('输入你的名字')
print(name)

