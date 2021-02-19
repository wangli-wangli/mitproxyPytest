# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://testapi.huxin315.com/cloud-service/api/merchant/myProject"
    header={'Host': 'testapi.huxin315.com', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTQyMzIwNjgsInVzZXJJZCI6Iklnbjd1aGZtcUV6ZkxsQmtoWENGNVI5cUc0c3lpWTNpU1dPWlpRbURENkkramJkY1FRTytBV3dUM2E2a1BVN1paTVlDc291aWhtSVlQZkdjcXlyZU9iTVNFK0UwRTlFM3ZodEMxeVBoa3IyN2hnc0crMEdudnBOcmdWOEYwMm5LZEd4dS9ZNGIxT1BTQ2F5aDEvZElRRmNyS1lCM3NvZzJKdHlHN0tBQjVsbz0iLCJpYXQiOjE2MTM2MjcyNjh9.nR7Zdx1UqiMef3ZelYNBFdqrXYHJrtSf2BvLFvWCUBwMgVHTBUzyNxiBlefJz2tspRInf4QVRH78UfEmxIhwwfy3B7v325mLYZnKTC1qfvG_U2P8l0JK_ew85yu5uDpUd1VijjpVUk4TXITmUmQlSInTm4YPjvSom0mVD-omOfqnk1k0gAXUGuNW6CFOERQs-ISrIm6k4P5BMvlDVUK9Z6RdDFNA5OddoU66ltTdhBo7PbGzhnzRJZ5T1Jiem4xvL3FtACCDRIlWcTj6MTXH4qrLAe6MwS9jpGYxSqRCHdYpAR6MqnNRAhtIkFhvKPiZnX5M0CFZlYPBYYPJfwGwmA', 'Content-Type': 'application/json;charset=UTF-8'}

    params={"pageNum":1}
    # json格式
    results = requests.post(url, headers=header,json=params).text
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
