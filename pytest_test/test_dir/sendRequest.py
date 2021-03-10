import requests
class interface:
    def __init__(self,url,headers,params):
        self.url=url
        self.headers=headers
        self.params=params
    def send_request(self):

        if self.headers["Content-Type"].find('json') >= 0:
            response = requests.post(
                self.url, headers=self.headers, json=self.params)
        else:
            response = requests.post(
                self.url, self.params, headers=self.headers)
        return response