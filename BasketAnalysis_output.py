# データフレームをオブジェクトにして処理する
# AND 条件による N数 を返す。
import itertools
import pandas as pd
import os
import numpy as np
import codecs
import datetime

# ディレクトリの変更
os.getcwd()
os.chdir("your_purchase_path")

# データの読み込み
# shift-jisだとread_csvできないので強引にとる
with codecs.open("your_purchase_path","r", "Shift-JIS", "ignore") as file:
    BasketData = pd.read_table(file, delimiter=",")
type(BasketData)
BasketData.head()
#BasketData = pd.read_csv("RowData.csv",index_col=0)

# 表頭名を取得。
Colnames = BasketData.columns.values
Colnames2 = BasketData.columns
DROPKEY = list(Colnames[[0,1,2,3,4,5]])
ColnamesDropped = Colnames2.drop(DROPKEY)
ColnamesDropped.values
ColnamesList = ColnamesDropped.values
len(ColnamesList)

# 表頭名の組合せのパタンを出す。
# 組合せた結果を出力する。
# 成分が組のリスト
Comb2 = list(itertools.combinations(ColnamesList,2))
Comb3 = list(itertools.combinations(ColnamesList,3))
Comb4 = list(itertools.combinations(ColnamesList,4))
Comb5 = list(itertools.combinations(ColnamesList,5))
Comb6 = list(itertools.combinations(ColnamesList,6))
Comb7 = list(itertools.combinations(ColnamesList,7))
Comb8 = list(itertools.combinations(ColnamesList,8))
Comb9 = list(itertools.combinations(ColnamesList,9))
Comb10 = list(itertools.combinations(ColnamesList,10))

'''
以下はComment Out
Comb11 = list(itertools.combinations(ColnamesList,11))
Comb12 = list(itertools.combinations(ColnamesList,12))
Comb13 = list(itertools.combinations(ColnamesList,13))
Comb14 = list(itertools.combinations(ColnamesList,14))
Comb15 = list(itertools.combinations(ColnamesList,15))
Comb16 = list(itertools.combinations(ColnamesList,16))
Comb17 = list(itertools.combinations(ColnamesList,17))
Comb18 = list(itertools.combinations(ColnamesList,18))
Comb19 = list(itertools.combinations(ColnamesList,19))
'''
Comb2 = pd.DataFrame(Comb2)
Comb3 = pd.DataFrame(Comb3)
Comb4 = pd.DataFrame(Comb4)
Comb5 = pd.DataFrame(Comb5)
Comb6 = pd.DataFrame(Comb6)
Comb7 = pd.DataFrame(Comb7)
Comb8 = pd.DataFrame(Comb8)
Comb9 = pd.DataFrame(Comb9)
Comb10 = pd.DataFrame(Comb10)

'''
以下はComment Out
Comb11 = pd.DataFrame(Comb11)
Comb12 = pd.DataFrame(Comb12)
Comb13 = pd.DataFrame(Comb13)
Comb14 = pd.DataFrame(Comb14)
Comb15 = pd.DataFrame(Comb15)
Comb16 = pd.DataFrame(Comb15)
Comb17 = pd.DataFrame(Comb15)
Comb18 = pd.DataFrame(Comb15)
Comb19 = pd.DataFrame(Comb15)
'''
# combN[列数][行数]
# 参照のために表頭名を格納
Colnames = pd.DataFrame(BasketData.columns.values)
# Colnames[0][21]
# sum(BasketData[Comb2[0][0]] * BasketData[Comb2[1][0]])

# プレ/ポストを出力。
PreData = BasketData[(BasketData[Colnames[0][4]] == 1) & (BasketData[Comb2[0][1]]==1) &(BasketData[Comb2[1][1]]==1)]
PreData.head()
PostData = BasketData[(BasketData[Colnames[0][4]] == 0) & (BasketData[Comb2[0][1]]==1) &(BasketData[Comb2[1][1]]==1)]
PostData.head()

'''
店舗名を返す
店舗名にIDを追加したほうがよさそうなので、データを追加する。
前ファイルのDROPKEY
''' 
BasketData[BasketData[Colnames[0][1]] == "***"]
BasketData[BasketData[Colnames[0][4]]==1][Comb2[0][1]]

# 分析実行。
# 型に厳しい。どうやら条件に合致しない組合せは空のデータフレームとして計上されて
# 厳しいらしい。
PreBox2 = []
PostBox2 = []
PreBox3 = []
PostBox3 = []
PreBox4 = []
PostBox4 = []
PreBox5 = []
PostBox5 = []
PreBox6 = []
PostBox6 = []
PreBox7 = []
PostBox7 = []
PreBox8 = []
PostBox8 = []
PreBox9 = []
PostBox9 = []
PreData[Comb2[0][0]] * PreData[Comb2[1][0]]

for i in range(len(Comb2)):
    X = sum(PreData[Comb2[0][i]] * PreData[Comb2[1][i]])
    Y = sum(PostData[Comb2[0][i]] * PostData[Comb2[1][i]])
    PreBox2.append(int(X))
    PostBox2.append(int(Y))
    
len(PreBox2)


for i in range(len(Comb3)):
    X = sum(PreData[Comb3[0][i]] * PreData[Comb3[1][i]]*\
    BasketData[Comb3[2][i]])
    Y = sum(PostData[Comb3[0][i]] * PostData[Comb3[1][i]]*\
    BasketData[Comb3[2][i]])
    PreBox3.append(int(X))
    PostBox3.append(int(Y))
    


for i in range(len(Comb4)):
    X = sum(BasketData[Comb4[0][i]] * BasketData[Comb4[1][i]] * \
    BasketData[Comb4[2][i]] * BasketData[Comb4[3][i]])
    AllBox4.append(int(X))

for i in range(len(Comb5)):
    X = sum(BasketData[Comb5[0][i]] * BasketData[Comb5[1][i]]* \
    BasketData[Comb5[2][i]]* BasketData[Comb5[3][i]]* \
    BasketData[Comb5[4][i]])
    AllBox5.append(int(X))

for i in range(len(Comb5)):
    X = sum(BasketData[Comb5[0][i]] * BasketData[Comb5[1][i]]* \
    BasketData[Comb5[2][i]]* BasketData[Comb5[3][i]]* \
    BasketData[Comb5[4][i]])
    AllBox5.append(int(X))

for i in range(len(Comb6)):
    X = sum(BasketData[Comb6[0][i]] * BasketData[Comb6[1][i]]* \
    BasketData[Comb6[2][i]]* BasketData[Comb6[3][i]]* \
    BasketData[Comb6[4][i]]*BasketData[Comb6[5][i]])
    AllBox6.append(int(X))

for i in range(len(Comb7)):
    X = sum(BasketData[Comb7[0][i]] * BasketData[Comb7[1][i]]* \
    BasketData[Comb7[2][i]]* BasketData[Comb7[3][i]]* \
    BasketData[Comb7[4][i]]* BasketData[Comb7[5][i]]* \
    BasketData[Comb7[6][i]])

for i in range(len(Comb8)):
    X = sum(BasketData[Comb8[0][i]] * BasketData[Comb8[1][i]]* \
    BasketData[Comb8[2][i]]* BasketData[Comb8[3][i]]* \
    BasketData[Comb8[4][i]]* BasketData[Comb8[5][i]]* \
    BasketData[Comb8[6][i]]*BasketData[Comb8[7][i]])
    AllBox8.append(int(X))

for i in range(len(Comb9)):
    X = sum(BasketData[Comb9[0][i]] * BasketData[Comb9[1][i]]* \
    BasketData[Comb9[2][i]]* BasketData[Comb9[3][i]]* \
    BasketData[Comb9[4][i]]* BasketData[Comb9[5][i]]* \
    BasketData[Comb9[6][i]]*BasketData[Comb9[7][i]]*\
    BasketData[Comb9[8][i]])
    AllBox9.append(int(X))

print("---------------------------------------------------------")
[len(Comb6),len(AllBox6)]
[len(Comb7),len(AllBox7)]
[len(Comb8),len(AllBox8)]
[len(Comb9),len(AllBox9)]
[len(Comb10),len(AllBox10)]

Comb6['合計'] = AllBox6
Comb7['合計'] = AllBox7
Comb8['合計'] = AllBox8
Comb9['合計'] = AllBox9
Comb10['合計'] = AllBox10

Comb6.to_csv("Combinations6_sum.csv",encoding="shift-jis")
Comb7.to_csv("Combinations7_sum.csv",encoding="shift-jis")
Comb8.to_csv("Combinations8_sum.csv",encoding="shift-jis")
Comb9.to_csv("Combinations9_sum.csv",encoding="shift-jis")
Comb10.to_csv("Combinations10_sum.csv",encoding="shift-jis")
