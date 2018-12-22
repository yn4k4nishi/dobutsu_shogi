#coding:utf-8
import csv
import pandas as pd
import numpy as np

def play_game(csv1,csv2):
    ### 盤面
    # +--------+ a
    # | 0| 1| 2|
    # | 3| 4| 5|
    # | 6| 7| 8|
    # | 9|10|11|
    # +--------+ b
    # 座標                 0  1  2  3  4  5  6  7  8  9 10 11 
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
    kkp_a = np.loadtxt(csv1,delimiter=',')
    kkp_b = np.loadtxt(csv2,delimiter=',')

###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.csv","kkp_gene/gene_1.csv")    
