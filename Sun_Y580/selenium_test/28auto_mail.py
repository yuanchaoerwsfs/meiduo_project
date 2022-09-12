import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

subject = 'Python email test'
with open('mail.txt', 'rb') as f:
    send_att = f.read()
# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
att = MIMEText(send_att, 'text', 'utf-8')
att['Content-Type'] = 'application/c=octet-stream'
att['Content-Disposition'] = "attachment;filename='mail.txt'"
msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(att)


msg['from'] = 'yuanchaoer@126.com'
msg['to'] = 'sunqw@cashwaytech.com'
# 发送邮件
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(u'yuanchaoer@126.com', u'qq123456')
smtp.sendmail('yuanchaoer@126.com', 'sunqw@cashwaytech.com', msg.as_string())
smtp.quit()
