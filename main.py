#coding:utf-8
import csv
import pandas as pd

def play_game(csv1,csv2):
    ### 盤面
    # +--------+ a
    # | 0| 1| 2|
    # | 3| 4| 5|
    # | 6| 7| 8|
    # | 9|10|11|
    # +--------+ b
    # 座標        0  1  2  3  4  5  6  7  8  9 10 11 
    boad_a_LI = [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    boad_a_EL = [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    boad_a_GI = [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    boad_a_CH = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    boad_a_Ch = [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    boad_b_LI = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    boad_b_EL = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    boad_b_GI = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    boad_b_CH = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    boad_b_Ch = [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    
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
    gene_a = pd.read_csv(csv1).values.tolist()
    gene_b = pd.read_csv(csv2).values.tolist()
    # print(gene_A)

    


###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.csv","kkp_gene/gene_1.csv")    
