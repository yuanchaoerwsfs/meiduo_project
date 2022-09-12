# # 例题
# def calc():
#     for i in range(1, 5):
#         for j in range(1, 5):
#             for k in range(1, 5):
#                 if (i != j) and (i != k) and (j != k):
#                     print(i, j, k)
#
#
# calc()
#
# year = int(input('输入年'))
# month = int(input('输入月'))
# day = int(input('输入日'))
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
#
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print("输入有误")
# leap=0
# sum=sum+day
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap=1
# else:
#     leap=0
#
# if leap==1 and month>2:
#     sum=sum+1
# print(sum)
#
#
#
#
# x=int(input('输入X'))
# y=int(input('输入Y'))
# z=int(input('输入Z'))
#
# if x>y:
#     temp=x
#     x=y
#     y=temp
# elif x>z:
#     temp = x
#     x = z
#     z = temp
# elif y>z:
#     temp=y
#     y=z
#     z=temp
# print(x,y,z)
#
# l=[]
# for i in range(3):
#     x=int(input("输入三个数字"))
#     l.append(x)
# l.sort()
# print(l)

# a1 = [1, 2, 3]
# c1=[]
# b1 = a1[:]
# print(b1)
# print(id(b1))
# print(id(a1))
# print(id(c1))
#
# for i in range(1,10):
#     for y in range(1,10):
#         n=i*y
#         print("i*y="+str(n))
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.time())

for n in range(100,999):
    i = n // 100
    j = (n // 10)%10
    k = n%10
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)