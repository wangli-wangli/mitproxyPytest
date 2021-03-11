import pytest
import os
from config.conf import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
def sendEmail():
    # 授权码：HGDFAIMHMWDKQYWJ
    # 编写HTML类型的邮件正文
    att = MIMEText("11", 'text', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = '"attachment;filename='+reportDir+'"'

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg.attach(att)
    # 登录密码：2024410102
    # 发送邮件
    msg['from'] = 'wl15176128570@126.com'
    msg['to'] = '15176128570@139.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("wl15176128570@126.com", "ONYAVCCEYFNKOETP")
    smtp.sendmail("wl15176128570@126.com", "2024410102@qq.com", msg.as_string())
    smtp.quit()
    print("发送成功")
def main():
    #执行用例
    os.system(args)
    sendEmail()


if __name__ == '__main__':
    main()


