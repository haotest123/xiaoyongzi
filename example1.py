#coding:utf-8
import imaplib
import smtplib
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    password = "fsmnqmptdatkdfjf"
    email_host = "smtp.qq.com"
    send_user = "2804160559@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "anyong" + "<" + send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server =smtplib.SMTP_SSL()
        server.connect(email_host,465)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

if __name__ == '__main__':
    send = SendEmail()
    user_list = ['anyong@jingyougroup.com']
    sub = "测试邮件"
    content = "山楂树之恋"
    send.send_mail(user_list,sub,content)