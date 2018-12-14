#coding:utf-8
import csv

def read_gene():
    with open('kkp_gene/gene_0.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばしたい時

        for row in reader:
            print(row)          # 1行づつ取得できる
