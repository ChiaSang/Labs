
# 生成苹果日报词云
import sqlite3
from os import path

import jieba
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from scipy.misc import imread
# import jieba.posseg as pseg
from wordcloud import ImageColorGenerator, WordCloud


def extract_words():
    with open('news_title.txt', 'r', encoding='utf-8') as f:
        news_subjects = f.readlines()
    stop_words = set(
        line.strip() for line in open('news_title.txt', encoding='utf-8'))
    newslist = []
    for subject in news_subjects:
        if subject.isspace():
            continue
        word_list = jieba.cut(subject)
        for word in word_list:
            if not word in stop_words == 'n':
                newslist.append(word)
    d = path.dirname(__file__)
    background_image = np.array(Image.open("testpic1.jpg"))

    content = ''.join(newslist)
    Wordcloud = WordCloud(
        font_path='STFANGSO.TTF',
        background_color="white",
        width=700,
        height=480,
        mask=background_image,
        max_font_size=100).generate(content)
    image_colors = ImageColorGenerator(background_image)

    plt.imshow(
        Wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis('off')
    Wordcloud.to_file("wordcloud.jpg")
    plt.show()


def read_data():
    conn = sqlite3.connect('D:\\Documents\\Python\\applenews\\apple.db')
    cursor = conn.cursor()
    for title in cursor.execute('SELECT TITLE FROM APPLE;'):
        print(title[0])
        with open('news_title.txt', 'a', encoding='utf-8') as f:
            f.write(str(title[0]) + '\n')


if __name__ == "__main__":
    # read_data()
    extract_words()
