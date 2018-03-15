import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
from scipy.misc import imread
from wordcloud import WordCloud
def words():
    with open('weibo.txt', 'rb') as f:
        comment_weibo = f.readlines()
    stop_words = set(line.strip() for line in open('stop.txt'))
    comment_list = []
    for comment in comment_weibo:
        if comment.isspace():
            continue
        word_list = pseg.cut(comment)#分词
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                comment_list.append(word)
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "001.png"))#读取图像
    content = ' '.join(comment_list)
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey",  mask=mask_image, max_words=100).generate(content)
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
if __name__ =="__main__":
    words()
