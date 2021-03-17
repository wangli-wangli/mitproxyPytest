import pytest
import os
from config.conf import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from lxml import etree

def readHtml():
    print(htmlName)
    f=open(htmlName,'r',encoding='utf-8')
    f=f.read()
    print(f)
    return f

def sendEmail():
    # 授权码：HGDFAIMHMWDKQYWJ
    # 编写HTML类型的邮件正文
    msg=MIMEMultipart('mixed')
    content=readHtml()
    text_html = MIMEText(content, _subtype='html', _charset='utf-8')
    text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
    msg.attach(text_html)
    msg["Subject"] = subject
    # 登录密码：2024410102
    # 发送邮件
    msg['From'] = 'wl15176128570@126.com'
    msg['To'] = '15176128570@139.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("wl15176128570@126.com", "ONYAVCCEYFNKOETP")
    smtp.sendmail("wl15176128570@126.com", "2024410102@qq.com", msg.as_string())
    smtp.quit()
    print("发送成功")
def main():
    #执行用例
    os.system(args)
    #sendEmail()


if __name__ == '__main__':
    main()
    #pytest.main()


