import pandas as pd 
import numpy as np 
from collections import Counter
from matplotlib import pyplot as plt 
import csv

df = pd.read_csv('lec_2.csv')
ids = df['Responder_id']
lang = df['LanguagesWorkedWith']
lang_counter = Counter()
for item in lang:
    lang_counter.update(item.split(';'))

language = []
popularity = []

for item in lang_counter.most_common(20):
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()
plt.barh(language, popularity)
plt.xlabel('popularity')
plt.ylabel('language')
plt.title('Most Common Languages')
plt.tight_layout()
plt.show()
