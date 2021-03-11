from mitmproxy import ctx, http
import json


class Modify:
    def response(self, flow):
        if flow.request.url.startswith("https://testapi.huxin315.com"):
            # 获取响应的json字符串，转成python对象进行解析和修改
            response={
                "msg": "傻逼，谁让你这么调接口了！",
                "code": 500
            }
            #修改完成后，奖python对象转成json字符串，set进请求的响应体重发送给客户端
            flow.response.set_text(json.dumps(response))
            ctx.log.info('modify response')


addons = [
    Modify()
]
