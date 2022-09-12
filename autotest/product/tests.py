from django.test import TestCase

# Create your tests here.
'''
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''
cak = []


# 添加名片
def add_personnel():
    print('请输入添加名片信息')
    cak_test = []
    print('请输入名字')
    name = input()
    cak_test.append(name)
    print('请输入年龄')
    age = input()
    cak_test.append(age)
    print('请输入性别')
    sex = input()
    cak_test.append(sex)
    print('请输入手机号')
    iphone = input()
    cak_test.append(iphone)
    cak.append(cak_test)


file_copy = 'E:\Appium知识总结.txt'
file_copy_new = 'E:\Appium知识总结_copy.txt'


def copy_text():
    with open(file_copy, 'r', encoding='ANSI') as f:
        with open(file_copy_new, 'w', encoding='ANSI') as f1:
            for temp in f.readlines():
                f1.write(temp)
                print(temp)
            print('-' * 35)


def read_text():
    with open(file_copy_new, 'r', encoding='ANSI') as f2:
        for temp in f2.readlines():
            print(temp)


# add_personnel()
# print(cak)

copy_text()
read_text()
