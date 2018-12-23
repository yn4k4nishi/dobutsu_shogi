#coding:utf-8
import numpy as np
import random

def generate_gene(file_name):
    ### 遺伝子の作成
    #相手のライオンの位置:12
    #自分のライオンの位置:11
    #数の駒              : 8 
    #マス目の数          :12
    kkp_first = np.random.randint(1,100, size=(12,11,8,12))

    ### np.savetxt
    np.save(file_name,kkp_first)
    print("generate gene : "+ file_name)

    ### np.loadtxt
    # list = np.load(file_name)
    # print(list[0])


#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.npy')
generate_gene('kkp_gene/gene_1.npy')
# generate_gene('kkp_gene/gene_2.csv')
# generate_gene('kkp_gene/gene_3.csv')
# generate_gene('kkp_gene/gene_4.csv')
# generate_gene('kkp_gene/gene_5.csv')
