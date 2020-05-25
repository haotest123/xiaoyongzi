#coding:utf-8

import smtplib
import os.path
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# import warnings

class SendEmail:
    global send_user
    global email_host
    global password
    password = "ucsmxcxczrcsdggc"
    email_host = "smtp.qq.com"
    send_user = "2804160559@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "2804160559" + "<" + send_user + ">"

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        log_path = os.path.dirname(os.path.abspath('.')) + '/test_report/result.html'

        #log_path=os.path.abspath(os.path.dirname(__file__)).split('newPython')[0] + 'newPython/logs/'
        # log_name =log_path +'%s.log'%time.strftime('%Y_%m_%d')
        # # 构造附件（附件为txt格式的文本）
        att = MIMEText(open(log_path ,'rb').read(), 'base64', 'utf-8')

        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=%s.html'%time.strftime('%Y_%m_%d')
        message.attach(att)
        server = smtplib.SMTP_SSL()
        server.connect(email_host,465)# 启用SSL发信, 端口一般是465
        # server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()