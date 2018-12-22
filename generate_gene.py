#coding:utf-8
import numpy as np
import random
import math

def generate_gene(file_name):
    ### 遺伝子の作成
    kkp_first = np.random.randint(1,100, size=(12*11*4,12))

    ### np.savetxt
    np.savetxt(file_name,kkp_first,delimiter=',')
    print("generate gene : "+ file_name)

    ### np.loadtxt
    list = np.loadtxt(file_name,delimiter=',')
    
    ### 表示
    for i in list:
        print("       A        B        C")
        print(" ","-"*28)
        print("1 | ","{0:4.1f}".format(i[0]) ," | ","{0:4.1f}".format( i[1])," | ","{0:4.1f}".format( i[2])," |")
        print(" ","-"*28)
        print("2 | ","{0:4.1f}".format(i[3]) ," | ","{0:4.1f}".format( i[4])," | ","{0:4.1f}".format( i[5])," |")
        print(" ","-"*28)
        print("3 | ","{0:4.1f}".format(i[6]) ," | ","{0:4.1f}".format( i[7])," | ","{0:4.1f}".format( i[8])," |")
        print(" ","-"*28)
        print("4 | ","{0:4.1f}".format(i[9]) ," | ","{0:4.1f}".format(i[10])," | ","{0:4.1f}".format(i[11])," |")
        print(" ","-"*28)
        print()


#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.csv')
# generate_gene('kkp_gene/gene_1.csv')
# generate_gene('kkp_gene/gene_2.csv')
# generate_gene('kkp_gene/gene_3.csv')
# generate_gene('kkp_gene/gene_4.csv')
# generate_gene('kkp_gene/gene_5.csv')
