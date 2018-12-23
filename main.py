#coding:utf-8
# import pandas as pd
import numpy as np

def play_game(npy1,npy2):
    ### 盤面
    # +--------+ a
    # | 0| 1| 2|
    # | 3| 4| 5|
    # | 6| 7| 8|
    # | 9|10|11|
    # +--------+ b
    # 座標               0  1  2  3  4  5  6  7  8  9 10 11 
    boad_a = np.array([[ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #lion
                       [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #elephant
                       [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #giraffe
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   #chicken
                       [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]])  #chick

    boad_b = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]])
    
    #おける場所
    canput = np.ones(shape=12)
    for i in boad_a:
        canput -= i
    for i in boad_b:
        canput -= i
    # print(canput)

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
    kkp_a = np.load(npy1)
    kkp_b = np.load(npy2)

    ### 評価盤面の取得
    where_mLI = np.where(boad_a[0])
    where_eLI = np.where(boad_b[0])

    if where_mLI[0][0] < where_eLI[0][0]:
        a_value = kkp_a[where_eLI[0][0]][where_mLI[0][0]]
        b_value = kkp_b[where_mLI[0][0]][where_eLI[0][0]]
    else:
        a_value = kkp_a[where_eLI[0][0]][where_mLI[0][0]-1]
        b_value = kkp_b[where_mLI[0][0]][where_eLI[0][0]-1]
    
    ### 入力層の作成
    # どこに動けるか
    can_move_a = np.ones(shape=(8,12))
    for i in range(8):
        for j in range(5):
            can_move_a[i] -= boad_a[j]
    # ライオンについて
    
    
    print(can_move_a)

###########################################################
#####                  main                           #####
###########################################################
play_game("kkp_gene/gene_0.npy","kkp_gene/gene_1.npy")    
