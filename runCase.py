import requests, time, re
import json
import csv


class api:

    def __init__(self,tag,path,hostname,method,authoration,content_type,params):
        self.tag = tag
        self.path = path
        self.hostname = hostname
        self.method=method
        self.authoration = authoration
        self.content_type = content_type
        self.params = params


    def userApi(self):
        url = "https://" + self.hostname  + self.path
        headers = {  # 设置http头部信息
            'Host': self.hostname,
            'Authorization': self.authoration,
            'Content-Type': self.content_type,
        }
        print(url)
        # json格式
        if headers["Content-Type"].find('json') >= 0:
            print(headers)
            print(self.params)
            results = requests.post(
                url, headers=headers, json=self.params, timeout=1.5).text
        else:
            results = requests.post(
                url, self.params, headers=headers, timeout=1.5).text
        print(results)
        return results
        # self.assertResult(results)

#返回合同id
    def returnId(self, result):
        result_dic = json.loads(result)
        code = result_dic['code']
        results = result_dic['result']
        msg = result_dic['msg']
        ids=[]
        for i in result:
            if i.stateText=='已终止':
                ids.append(id)
        return ids



    # def assertResult(self,results):


if __name__ == '__main__':

    with open(r'C:\Users\ZL-52S8FFG\Desktop\new2.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i in reader:
            api2=api(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            result=api2.userApi()


