import pytest
import json
import requests
import allure
from  sendRequest import interface


@pytest.mark.发行计划
def test_api():
    url = "https://testapi.huxin315.com//cloud-service/api/merchant/myProject"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params={"pageNum":1}
    params_byte=json.dumps(params,indent=4).encode()
    headers_bype=json.dumps(headers,indent=4).encode()
    url_bype = url.encode()
    send_request=interface(url,headers,params)
    response=send_request.send_request()

    response_text=response.text
    response_json=json.loads(response_text)
    response_byte = json.dumps(response_json, ensure_ascii=False,indent=4)
    allure.attach(url_bype, "url:", allure.attachment_type.JSON)
    allure.attach(headers_bype, "headers:", allure.attachment_type.JSON)
    allure.attach(params_byte, "请求参数:", allure.attachment_type.JSON)
    allure.attach(response_byte, "响应参数:", allure.attachment_type.JSON)
    allure.attach(str(response.status_code).encode(), "状态码:", allure.attachment_type.JSON)
    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)
    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



