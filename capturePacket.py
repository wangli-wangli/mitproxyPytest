from mitmproxy import ctx
import csv
# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):
    # 获取请求对象
    request = flow.request
    # 实例化输出类
    info = ctx.log.info
    # 打印请求的url
    # 实例化输出类
    filter_url='testapi.huxin315.com'
    if request.host==filter_url:
        info('host----'+request.url)
        with open(r'C:\Users\ZL-52S8FFG\Desktop\new2.csv', 'a', newline='', encoding='utf-8') as f2:
            csv_writer = csv.writer(f2)
            csv_writer.writerow([request.url, request.host,request.port,request.headers,request.cookies,request.get_text()])
            f2.close()
    # 打印请求方法
        #info(request.method)
    # # 打印host头
        info('host----'+request.host)
    # # 打印请求端口
        #info(str(request.port))
    # # 打印所有请求头部
        #info(str(request.headers))
    # # 打印cookie头
        #info(str(request.cookies))

# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    # 获取响应对象
    response = flow.response
    # 实例化输出类
    info = ctx.log.info
    with open(r'C:\Users\ZL-52S8FFG\Desktop\new2.csv', 'a', newline='', encoding='utf-8') as f2:
        csv_writer = csv.writer(f2)
        csv_writer.writerow([response.status_code, response.headers, response.cookies, response.text])
        f2.close()
    # 打印响应码
    # info(str(response.status_code))
    # # 打印所有头部
    # info(str(response.headers))
    # # 打印cookie头部
    # info(str(response.cookies))
    # 打印响应报文内容
    #info(str(response.text))