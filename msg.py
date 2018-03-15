import requests

class GetMSG:
    def __init__(self):
        
        self.url = 'https://zhuanlan.zhihu.com/api/columns/catwho/followers'

        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def getFenSi(self, param):

        self.html = requests.get(self.url, params=param, headers=self.header)

        for n in range(20):    

            hashData = self.html.json()[n]['hash']

            self.data2File(hashData)
    
    # 保存数据到本地

    def data2File(self, data):

        with open('F:\python_work\爬虫/hash.txt', 'a') as f:
            f.write(data+'\n')

if __name__ == '__main__':

    getmsg = GetMSG()

    for m in range(0, 40, 20):

        param = {'limit': 20,
                 'offset': m}

        getmsg.getFenSi(param)

