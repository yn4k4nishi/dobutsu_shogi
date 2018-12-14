#coding:utf-8
import csv
import pandas as pd

<<<<<<< HEAD
def update_boad(boad,hand,gene):
    elion = boad.index(-1)
    mlion = boad.index(1)
    if elion < mlion:
        # kkp_lion     = gene[(elion*11 + mlion -1)*5]
        kkp_elephant = gene[(elion*11 + mlion -1)*5]
        kkp_giraffe  = gene[(elion*11 + mlion -1)*5 +1]
        kkp_checken  = gene[(elion*11 + mlion -1)*5 +2]
        kkp_check    = gene[(elion*11 + mlion -1)*5 +3]
    else:
        # kkp          = gene[(elion*11 + mlion)*5]
        kkp_elephant = gene[(elion*11 + mlion)*5]
        kkp_giraffe  = gene[(elion*11 + mlion)*5 +1]
        kkp_checken  = gene[(elion*11 + mlion)*5 +2]
        kkp_check    = gene[(elion*11 + mlion)*5 +3]
    
    kkp_elephant.insert(elion ,0)
    kkp_elephant.insert(mlion ,0)
    kkp_giraffe.insert(elion,0)
    kkp_giraffe.insert(mlion,0)
    kkp_checken.insert(elion,0)
    kkp_checken.insert(mlion,0)
    kkp_check.insert(elion,0)
    kkp_check.insert(mlion,0)

    ## 現在の局面を計算
    melephant = boad.index(2)
    mgiraffe  = boad.index(3)
    mcheckin  = boad.index(4)
    mcheck    = boad.index(5)
    

def play_game(csv1,csv2):
    ### 盤面
    # +--------+
    # | 0| 1| 2|
    # | 3| 4| 5|
    # | 6| 7| 8|
    # | 9|10|11|
    # +--------+
    # Aのライオン :  1
    # Aのゾウ     :  2
    # Aのキリン   :  3
    # Aのニワトリ :  4
    # Aのヒヨコ   :  5
    # Bのライオン : -1
    # Bのゾウ     : -2
    # Bのキリン   : -3
    # Bのニワトリ : -4
    # Bのヒヨコ   : -5
    # なにもないところは 0
    boad = [-3,-1,-2,0,-5,0,0,5,0,2,1,3]
 
    ###持ち駒 [ライオン, ゾウ, キリン, ヒヨコ]
    a_hand = [0,0,0,0]
    b_hand = [0,0,0,0]

    ###駒得の得点
    point_lion = 10000
    point_elephant = 25
    point_giraffe = 25
    point_checkin = 10
    point_check = 5
    ### KKPの読み込み
    gene_A = pd.read_csv(csv1).values.tolist()
    gene_B = pd.read_csv(csv2).values.tolist()
    # print(gene_A)






###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.csv","kkp_gene/gene_1.csv")    
=======
#   盤面
# +--------+
# | 1| 2| 3|
# | 4| 5| 6|
# | 7| 8| 9|
# |10|11|12|
# +--------+

# Aのライオン :  1
# Aのゾウ     :  2
# Aのキリン   :  3
# Aのニワトリ :  4
# Aのヒヨコ   :  5
# Bのライオン : -1
# Bのゾウ     : -2
# Bのキリン   : -3
# Bのニワトリ : -4
# Bのヒヨコ   : -5
# なにもないところは 0
boad = [-3,-1,-2,0,-5,0,0,5,0,2,1,3]

geneA = pd.read_csv("kkp_gene/gene_0.csv").values.tolist()
geneB = pd.read_csv("kkp_gene/gene_1.csv").values.tolist()
# print(geneA)

def checkmate():
>>>>>>> 915528b8443acdf3c27f8175add042b6a7645a35
