from do_excel import Do_Excel
import requests

# 设置消息头
headers = {"Content-Type": "application/json"}
xls_dic = Do_Excel().read_excel()  # 读取表格自定义字段
funcdata_list = xls_dic["功能报文"]  # “功能列表”的所有值
url_list = xls_dic["测试地址"]  # “测试地址”的所有值

for i in range(xls_dic["行数"] - 1):
    response = requests.post(url_list[i], headers=headers, data=funcdata_list[i])
    print(response.status_code)
    print(response.text)
