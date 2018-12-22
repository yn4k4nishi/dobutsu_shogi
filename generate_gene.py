#coding:utf-8
import numpy as np
import random

def generate_gene(file_name):
    ### 遺伝子の作成
    #相手のライオンの位置:12
    #自分のライオンの位置:11
    #ライオン以外の駒    : 4
    #KK                  :12
    kkp_first = np.random.randint(1,100, size=(12,11,5,12))

    ### np.savetxt
#   np.savetxt(file_name,kkp_first,delimiter=',')
    np.save(file_name,kkp_first)
    print("generate gene : "+ file_name)

    ### np.loadtxt
#     list = np.loadtxt(file_name,delimiter=',')
    list = np.load(file_name)
    print(list[0])


#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.npy')
# generate_gene('kkp_gene/gene_1.csv')
# generate_gene('kkp_gene/gene_2.csv')
# generate_gene('kkp_gene/gene_3.csv')
# generate_gene('kkp_gene/gene_4.csv')
# generate_gene('kkp_gene/gene_5.csv')
