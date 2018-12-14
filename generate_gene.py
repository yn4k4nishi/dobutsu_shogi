#coding:utf-8
import numpy as np
import random
import csv

kkp_first = np.random.randint(100, size=(12,12*11*5))

print(kkp_first)

with open('kkp.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    # writer.writerow(list)     # list（1次元配列）の場合
    writer.writerows(kkp_first) # 2次元配列も書き込める