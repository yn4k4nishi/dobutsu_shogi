#coding:utf-8
import numpy as np
import random
import csv

def generate_gene(csvfile):
    ### 遺伝子の作成
    kkp_first = np.random.randint(100, size=(12*11*5,12-2))
    # kkp_first[0][0] = None
    # print(kkp_first)

    ### CSVファイルに書き込み
    with open(csvfile, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(kkp_first)
    print("generate gene : "+ csvfile)

#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.csv')
generate_gene('kkp_gene/gene_1.csv')
generate_gene('kkp_gene/gene_2.csv')
generate_gene('kkp_gene/gene_3.csv')
generate_gene('kkp_gene/gene_4.csv')
generate_gene('kkp_gene/gene_5.csv')
