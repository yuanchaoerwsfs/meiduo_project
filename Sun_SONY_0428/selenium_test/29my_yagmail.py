import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user='yuanchaoer@126.com', password='qq123456', host='smtp.126.com')
# 邮箱正文
contents = ['This is the body,and here is just text http://somedomain/image.png', 'You can find an audio file attached']
# 发送邮件
yag.send('sunqw@cashwaytech.com', 'Subject', contents, ['d:/user_info.txt'])
