import csv
import codecs
from itertools import islice

# 读取csv文件
data = csv.reader(codecs.open("d:/python3-test//material/userinfo.csv", 'r', 'gbk'))
# 存放用户数据
users =[]
# 循环输出每行信息
for line in islice(data, 1, None):
    users.append(line)
# 打印
print(users)
