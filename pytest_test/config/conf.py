import time
import os
projectDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now_time=time.strftime("%Y%m%d_%H")
# 报告目录
reportDir = os.path.join(projectDir, 'report')
#邮箱配置信息
#邮箱服务器
smtpServer='smtp.126.com'
#发送者
fromUser='"wl15176128570@126.com'
#发送者密码
fromPassWord='HGDFAIMHMWDKQYWJ'
#接受者
toUser='2024410102@qq.com'
#邮件标题
subject='测试报告'
#邮件正文
contents='正文'
#报告名称
htmlName =reportDir+"\\"+now_time+"report.html"

#脚本执行命令
args='pytest --html='+htmlName