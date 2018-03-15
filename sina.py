import requests
import re
import time
def sinaname(ID, pages):
    ii = 0
    k = 1
    while ii <= int(pages):
        ii = ii+1
        url_next='https://m.weibo.cn/api/comments/show?id='+ID+'&page='+str(ii)
        html=requests.get(url_next)  # 请求网址信息
        for jj in range(0, len(html.json()['data'])):
            print(jj)
            data1 = html.json()['data']['data'][jj]['text']
            print(data1)
            with open('F:\\python\ciyun\\weibo.txt', 'a', encoding='utf-8') as ff:
                hanzi = ''.join(re.findall('[\u4e00-\u9fa5]', data1))
                ff.write(hanzi+'\n')
                print("已经写入%d个信息" % k)
                k += 1
            time.sleep(1)
id = '4198647488971144'
page = '200'
sinaname(id, page)
