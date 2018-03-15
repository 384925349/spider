import requests


class GetMSG:
    def __init__(self):
        self.url = 'https://usercollection.chinadaily.com.cn/uac?icb_uac=icb_uac&d=hj85tX2eCWqtbkTu22SoMit+M/JXv7bwyslDHl0nqCS2rtpSulNTb2Yt588E9fDgK4Y+M2iVoWcCAT2/y3a2ar011/U1vDu8&_aid=08ec94a88d26dabb0e8a43a7098d2c01&_=1521011032866'

        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        #response = requests.get(url)


    def getSY(self, param):
        self.html = requests.get(self.url, params=param, headers=self.header)

        hashData = self.html.json()[n]['hash']

        self.dataFile(hashData)

        def dataFile(self, data):
            with open('F:\python_work\爬虫/123.txt', 'a') as f:
                f.write(data + '\n')
if __name__ == '__main__':

    getmsg = GetMSG()

    param = {'limit': 20,'offset': m}

        getmsg.getSY(param)