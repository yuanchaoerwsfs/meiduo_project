from itertools import islice
import csv
import codecs

base = ['sun', 'quan', 'wei', '汉', '天津市河东区']
print(base)
# print(base[0].title())
# print(base[1].title())
# print(base[2].title())
base.append('恒银金融科技股份')
# print(base[-1])
with codecs.open('d:/Sun/selenium_test/csv.csv', 'r', 'utf-8') as f:
    ret = f.readable()
    print(ret)
    data = csv.reader(f)
    for line in islice(data, 1, None):
        base.append(line)
print(base)
# print(base[-1])
with codecs.open('d:/Sun/selenium_test/csv.csv', 'a', 'utf-8') as f1:
    data = csv.reader(f1)
    line = '白大傻'
    f1.write(line)  # 写入后立刻打印无法打印出新添加数据，需在下次打开后才可以打印新增数据
    print(base)
#    print(base[-1])
base.insert(4, '白狗狗')
print(base)
del base[-1]
base_pop = base.pop()      #从尾部弹出元素，并且可以通过变量获取被弹出元素值
print(base)
print(base_pop)
base.remove('白狗狗')
print(base)
base.sort()
print(base)



