import pytest
import json
from  sendRequest import interface
from interface_parms import api_val
@pytest.mark.发行计划
def test_test_issuance_plan0():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/merchant/myProject"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan1():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectByUser"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":1,"authState":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan2():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectByUser"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":2,"authState":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan3():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectByUser"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":3,"authState":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan4():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectByUser"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":4,"authState":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan5():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/yfsAgreeGroup/optList"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"entId":"d946d4eb4c6662628ddb21f3ff10729f","corBusiness":0}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan6():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/shop/selectShopByEntId"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='entId=d946d4eb4c6662628ddb21f3ff10729f'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan7():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectEntById"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='entId=d946d4eb4c6662628ddb21f3ff10729f&isPro=true'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan8():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/yfsAgreement/queryInfo"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='argName=%E5%8F%91%E8%A1%8C%E8%AE%A1%E5%88%92%E6%89%BF%E8%AF%BA%E4%B9%A6&entId=d946d4eb4c6662628ddb21f3ff10729f'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan9():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/comm/entTagInfo"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='entno=123456789014632748'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan10():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/merchant/insertProject"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"yfsProject":{"entId":"d946d4eb4c6662628ddb21f3ff10729f","proName":"【测试计划A】","startTime":1613577600000,"endTime":1646063999000,"serverStopTime":1646036784901,"joinIns":true,"isVoucher":false,"isDis":false,"prepaidLimit":"10","consume":3,"productForm":0,"useScope":0,"registered":0,"phoneNumbers":"jCOspwyLYVAJE9YCV9VXn0ORuLMSIgp/+84PI9Vs7umKHCl9wg/BebSeec/+I3Gb/U59SPVTGzRg8izgrwMSkvCIPAMRMlAkuXus/fBBVe3rT4Ayjltg0VitwBMTRlFyfvlTaGqGSH5QppBRr+Jq4GeW9sA/rfbIwd4vb5FXLDE=","verCode":"000000","proAbstract":"服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容服务内容","shopIds":["ebb6a3c3e82d13b73f97d3f0f224ce47"],"agrId":"cf17a89f131a86b97ce329d34745fa10","totalPri":"1000","lastUpdateTime":"2021-02-18T14:31:36"},"verCode":"000000"}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan11():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/merchant/myProject"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan12():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/project/queryInfo"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='id=11b372274353e8b803690b63de70fe88'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan13():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/merchant/queryByProNo"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='pageNum=1&proNo=ee495b-2021-ef6b'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan14():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/yfsSecurityRecord/list"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    params='{"pageNum":1,"busiIds":"11b372274353e8b803690b63de70fe88","status":1}'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan15():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/agreeGroup/queryInfo"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='id=cf17a89f131a86b97ce329d34745fa10'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



@pytest.mark.发行计划
def test_test_issuance_plan16():
    '''发行计划'''
    url = "https://testapi.huxin315.com/cloud-service/api/enterprise/selectEntById"
    headers = {  # 设置http头部信息
        'Host': 'testapi.huxin315.com',
        'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    params='entId=d946d4eb4c6662628ddb21f3ff10729f'
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

    msg = response_json["msg"]
    code = response_json["code"]
    code_str=str(code)

    assert response.status_code == 200
    assert code_str != '0'
    assert code_str[0] !='3' #3xx-重定向：客户端浏览器必须采取更多操作来实现请求。
    assert code_str[0] != '4' #4xx-客户端错误：发生错误，客户端似乎有问题。
    assert code_str[0] != '5' #5xx-服务器错误：服务器由于遇到错误而不能完成该请求。



