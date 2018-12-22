#coding:utf-8
import numpy as np
import random
import math
import time

def find_LI(place):
        if place == -1:
                print("   LI   |",end='')
        elif place == -2:
                print("  *LI   |",end='')
        else:
                print("  {0:4.1f}  |".format(place),end='')

def which_ani(num):
        if num > 12*11*4:
                print("[ NUMBER:{0:2d} ] KK".format(num))
        elif num % 4 == 1:
                print("[ NUMBER:{0:2d} ] ゾウのKKP".format(num))
        elif num % 4 == 2:
                print("[ NUMBER:{0:2d} ] キリンのKKP".format(num))
        elif num % 4 == 3:
                print("[ NUMBER:{0:2d} ] ニワトリのKKP".format(num))
        else:
                print("[ NUMBER:{0:2d} ] ヒヨコのKKP".format(num))

def generate_gene(file_name):
    ### 遺伝子の作成
    #相手のライオンの位置:12
    #自分のライオンの位置:11
    #ライオン以外の駒    : 4
    #KK                  :12
    kkp_first = np.random.randint(1,100, size=(12*11*4+12,12))
    for a in range(12):
            for b in range(11):
                    for c in range(4):
                            kkp_first[a*11*4+b*4+c][a] = -2
                    if a > b:
                            for c in range(4):
                                kkp_first[a*11*4+b*4+c][b] = -1
                    else:
                            for c in range(4):
                                kkp_first[a*11*4+b*4+c][b+1] = -1                   

    ### np.savetxt
    np.savetxt(file_name,kkp_first,delimiter=',')
    print("generate gene : "+ file_name)

    ### np.loadtxt
    list = np.loadtxt(file_name,delimiter=',')
    
    ### 表示
#     for i in list:
#         print("       A        B        C")
#         print(" ","-"*28)
#         print("1 | ","{0:4.1f}".format(i[0]) ," | ","{0:4.1f}".format( i[1])," | ","{0:4.1f}".format( i[2])," |")
#         print(" ","-"*28)
#         print("2 | ","{0:4.1f}".format(i[3]) ," | ","{0:4.1f}".format( i[4])," | ","{0:4.1f}".format( i[5])," |")
#         print(" ","-"*28)
#         print("3 | ","{0:4.1f}".format(i[6]) ," | ","{0:4.1f}".format( i[7])," | ","{0:4.1f}".format( i[8])," |")
#         print(" ","-"*28)
#         print("4 | ","{0:4.1f}".format(i[9]) ," | ","{0:4.1f}".format(i[10])," | ","{0:4.1f}".format(i[11])," |")
#         print(" ","-"*28)
#         print()

    counter = 0
    ### 表示
    print()
    for i in list:
        counter += 1
        which_ani(counter)
        print("       A        B        C")
        print(" ","-"*28)
        print("1 |",end='')
        find_LI(i[0])
        find_LI(i[1])
        find_LI(i[2])
        print()
        print(" ","-"*28)
        
        print("2 |",end='')
        find_LI(i[3])
        find_LI(i[4])
        find_LI(i[5])
        print()
        print(" ","-"*28)
        
        print("3 |",end='')
        find_LI(i[6])
        find_LI(i[7])
        find_LI(i[8])
        print()
        print(" ","-"*28)
        
        print("4 |",end='')
        find_LI(i[9])
        find_LI(i[10])
        find_LI(i[11])
        print()
        print(" ","-"*28)
        print()

        if counter % 4 == 0:
                print("********************************************")
        #         time.sleep(3)


#############################################
#####               main                #####
#############################################
generate_gene('kkp_gene/gene_0.csv')
# generate_gene('kkp_gene/gene_1.csv')
# generate_gene('kkp_gene/gene_2.csv')
# generate_gene('kkp_gene/gene_3.csv')
# generate_gene('kkp_gene/gene_4.csv')
# generate_gene('kkp_gene/gene_5.csv')
