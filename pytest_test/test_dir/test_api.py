import pytest
import json
from  sendRequest import interface

from interface_parms import api_val


@pytest.mark.发行计划
def test_api():
    url = "https://testapi.huxin315.com//cloud-service/api/merchant/myProject"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE3MDIyODc4NTMsInVzZXJJZCI6ImJtZnk1eGFhSU1uUkdQa3dvR0VXTkNITEhmeFkyUW8wL2sxN0NwWGRLQ3dzbmc3RVhhaHdBbWlnUG5FOWl5VkF2YTBrR2NpeVQ0VjJEYTh2U20rQndzc2lxeGhQNHZXT3RnYys2VnR4Wng5TXV1a3lua29WK3FoOWhEaklGSVN3dEF0T29EL1FIV04xTGV4QnhlTForbjhEaWI1NlZ5akhGUkwzZDhEU2hlST0iLCJpYXQiOjE2MTU5NzQyNTN9.vi-vY0wEVAll1MWTZ4A5G6KKkDbnEBuDB2qZkyGc6fBcq8CzUIQiK7H5WspcQOESVYV-od9a-6-BVxGPgJDGd5zreiT--dUWoOkZ7TCq8pShIaOj1nVafKBWkMEiT5UdO4Cojmb9P0Svnmp7KltZbx43fINH4cMgBDnpGZnpcjIS_u-9vQd3ld76a4cR_adrOmr8zcJ9wcndQetaqdNmQCfbjIRqMaEPzzP2HrvfIrrK7wbitrx7F0JA6zbAEbpaR2Oa0qj-_CFQjYeNYiST7vG0Dl7LhWOJHSST5hAl8DG5HXKoBK8s1CAt1TYWcfmyi-6sZBAN_Z4ti7S5yqc-Wg',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params={"pageNum":1}
    send_request=interface(url,headers,params)
    response=send_request.send_request()

    response_text=response.text
    response_json=json.loads(response_text)
    api_val.reponse = response_text
    api_val.statue_code = response.status_code
    api_val.url=url
    api_val.request=params
    print(response_text)
    print("###########",api_val.url)



    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



