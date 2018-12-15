#coding:utf-8
import csv
import pandas as pd
import numpy as np

def make_kkp(lion_a,lion_b,gene):
    white_lion = np.where(lion_a==1)
    black_lion = np.where(lion_b==1)
    kkp = np.zeros((4,12))
    if white_lion < black_lion:
        kkp[0] = gene[white_lion * 11 * 4 + black_lion - 1]
        kkp[1] = gene[white_lion * 11 * 4 + black_lion - 1 + 1]
        kkp[2] = gene[white_lion * 11 * 4 + black_lion - 1 + 2]
        kkp[3] = gene[white_lion * 11 * 4 + black_lion - 1 + 3]
    else:
        kkp[0] = gene[white_lion * 11 * 4 + black_lion ]
        kkp[1] = gene[white_lion * 11 * 4 + black_lion + 1]
        kkp[2] = gene[white_lion * 11 * 4 + black_lion + 2]
        kkp[3] = gene[white_lion * 11 * 4 + black_lion + 3]
    
    return kkp


def play_game(csv1,csv2):
    ### 盤面
    # +--------+ a
    # | 0| 1| 2|
    # | 3| 4| 5|
    # | 6| 7| 8|
    # | 9|10|11|
    # +--------+ b
    # 座標        0  1  2  3  4  5  6  7  8  9 10 11 
    boad_a_LI = np.array([ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    boad_a_EL = np.array([ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    boad_a_GI = np.array([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    boad_a_CH = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    boad_a_Ch = np.array([ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])

    boad_b_LI = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
    boad_b_EL = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
    boad_b_GI = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    boad_b_CH = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    boad_b_Ch = np.array([ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    
    ###持ち駒 [ライオン, ゾウ, キリン, ヒヨコ]
    a_hand = np.array([ 0,0,0,0])
    b_hand = np.array([ 0,0,0,0])

    ###駒得の得点
    point_LI = 10000
    point_EL = 25
    point_GI = 25
    point_CH = 10
    point_Ch = 5

    ### KKPの読み込み
    # gene_a = pd.read_csv(csv1).values.tolist()
    # gene_b = pd.read_csv(csv2).values.tolist()
    # print(gene_A)

    # kkp_a = make_kkp(boad_a_LI,boad_b_LI,gene_a)
    # kkp_b = make_kkp(boad_a_LI,boad_b_LI,gene_b)

    # a_score = kkp_a[0]*boad_a_EL + kkp_a[1]*boad_a_GI + kkp_a[2]*boad_a_CH + kkp_a[3]*boad_a_Ch
    # b_score = kkp_b[0]*boad_b_EL + kkp_b[1]*boad_b_GI + kkp_b[2]*boad_b_CH + kkp_b[3]*boad_b_Ch
    # print(a_score,b_score)

###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.csv","kkp_gene/gene_1.csv")    
