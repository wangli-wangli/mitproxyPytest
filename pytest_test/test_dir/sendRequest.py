import requests
class interface:
    def __init__(self,url,headers,params,method):
        self.url=url
        self.headers=headers
        self.params=params
        self.method=method
    def send_request(self):
        if self.method=='get':
            self.getApi()
        else:
            self.postApi()

    def postApi(self):

        if self.headers["Content-Type"].find('json') >= 0:
            response = requests.post(
                self.url, headers=self.headers, json=self.params)
        else:
            response = requests.post(
                self.url, self.params, headers=self.headers)
        return response

    def getApi(self):
        if self.headers["Content-Type"].find('json') >= 0:
            response = requests.get(
                self.url, headers=self.headers, json=self.params)
        else:
            response = requests.get(
                self.url, self.params, headers=self.headers)
        return response