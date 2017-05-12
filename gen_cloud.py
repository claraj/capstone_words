from wordcloud import WordCloud
#from config import all_text_file

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt    ## hrr. https://github.com/tensorflow/tensorflow/issues/2375

text = open('allwords.txt').read()

wordcloud = WordCloud().generate(text)


image = wordcloud.to_image()

wordcloud.to_file('capstone_words.bmp')

image.show()
