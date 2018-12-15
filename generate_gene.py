#coding:utf-8
import numpy as np
import random

def generate_gene(file_name):
    ### 遺伝子の作成
    kkp_first = np.random.randint(100, size=(12*11*4,12-2))
    # kkp_first[0][0] = None
    # print(kkp_first)

    ### np.savetxt
    np.savetxt(file_name,kkp_first,delimiter=',')
    print("generate gene : "+ file_name)

    ### np.loadtxt
    # list = np.loadtxt(file_name,delimiter=',')
    # print(list)
    # print("\n")


#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.csv')
generate_gene('kkp_gene/gene_1.csv')
generate_gene('kkp_gene/gene_2.csv')
generate_gene('kkp_gene/gene_3.csv')
generate_gene('kkp_gene/gene_4.csv')
generate_gene('kkp_gene/gene_5.csv')
