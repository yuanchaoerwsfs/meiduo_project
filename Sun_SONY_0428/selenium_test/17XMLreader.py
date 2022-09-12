from xml.dom.minidom import parse
#打开XML文件
dom = parse("d:/python3-test/material/config.xml")
#获取xml中元素
root = dom.documentElement
#获取标签
tag_name = root.getElementsByTagName('platform')
login_info = root.getElementsByTagName('login')

print(tag_name[0].firstChild.data)  #//根据标签获取一组标签
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)

username=login_info[0].getAttribute('username')
username1=login_info[1].getAttribute('username')
password=login_info[0].getAttribute('password')
password1=login_info[1].getAttribute('password')
print(username)
print(username1)
print(password)
print(password1)