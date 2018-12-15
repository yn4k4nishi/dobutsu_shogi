#coding:utf-8
import csv
import pandas as pd

def make_kkp(lion_a,lion_b,gene):
    white_lion = lion_a.index(1)
    black_lion = lion_b.index(1)
    if white_lion < black_lion:
        kkp_EL = gene[white_lion * 11 * 4 + black_lion - 1]
        kkp_GI = gene[white_lion * 11 * 4 + black_lion - 1 + 1]
        kkp_CH = gene[white_lion * 11 * 4 + black_lion - 1 + 2]
        kkp_Ch = gene[white_lion * 11 * 4 + black_lion - 1 + 3]
    else:
        kkp_EL = gene[white_lion * 11 * 4 + black_lion ]
        kkp_GI = gene[white_lion * 11 * 4 + black_lion + 1]
        kkp_CH = gene[white_lion * 11 * 4 + black_lion + 2]
        kkp_Ch = gene[white_lion * 11 * 4 + black_lion + 3]

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
    point_LI = 10000
    point_EL = 25
    point_GI = 25
    point_CH = 10
    point_Ch = 5

    ### KKPの読み込み
    gene_a = pd.read_csv(csv1).values.tolist()
    gene_b = pd.read_csv(csv2).values.tolist()
    # print(gene_A)


###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.csv","kkp_gene/gene_1.csv")    
