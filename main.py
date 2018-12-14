#coding:utf-8
import csv
import pandas as pd

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
boad = [-3,-1,-2,0,-5,0,]

geneA = pd.read_csv("kkp_gene/gene_0.csv").values.tolist()
geneB = pd.read_csv("kkp_gene/gene_1.csv").values.tolist()
# print(geneA)

def checkmate():