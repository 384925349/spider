from requests import get
from urllib import parse

pictureLeiXing = input('类型：')
pictureNumber = int(input('页数：'))
pictureName = parse.quote(pictureLeiXing)

for m in range(0, pictureNumber):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+pictureName+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn='+str(m*30)+'&rn=30&gsm=1e&1520960853143='
    html = get(url)
    #response = requests.get(url)
    #html = response.text


    for n in range(30):
        pictureUrl = html.json()["data"][n]["middleURL"]
        print(pictureUrl[-20:])
        picture = get(pictureUrl).content
        with open('F:/python_work/picture/'+pictureUrl[-20:], 'wb') as ff:
            ff.write(picture)
