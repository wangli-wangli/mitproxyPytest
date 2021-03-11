# mitmproxyAllureProject
技术点：mitmproxy+pytest+allure
自动抓包，利用模板生成测试用例，allure展示测试报告
# 安装使用allure

## 安装allure:下载地址:https://github.com/allure-framework/allure2/releases

在官网上下载，对应的版本到本地，解压出来

## 添加path环境变量
打开\allure-2.8.0\bin文件夹，会看到allure.bat文件，讲此路径设置为系统环境变量path下，这样cmd任意目录都能执行了


## 校验是否安装成功
在cmd中运行 allure命令，
## 在已经写好的脚本文件中，在reports目录下新建一个pytest.ini文件

文件内容如下
[pytest]
'''
addopots=-s -q --alluredir=./allure-results #运行python脚本，把运行的xml结果放在allure-results文件中testpaths=./test_run\tripartiteServices\rechargeinterface\rechargeoil #要运行的测试用例路径python_files=test_.py # 运行的py文件是以test开头的
python_classes=test_ # 运行的类是以test开头的
python_functions=test_* # 运行的函数是以test开头的
'''
## 打开pycharm的terminal模式，运行 pytest命令，就可以看到测试用例的执行结果了，且在allure-results生成了xml格式的测试报告
## 运行 allure generate directory-with-results/ -o directory-with-report命令，生成allure的测试报告。
directory-with-report是指文件名称
比如我的测试报告放在项目目录下就执行 allure generate allure-results/ -o allure-report
## 运行成功后，在allure-report文件夹下找到index.html，选择谷歌运行


