# 遺伝的アルゴリズム
* KKP,KKを採用

# 盤面評価について
* 相手と自分のライオンの位置で予め持っていいるKK,KKP(遺伝子)で盤面を評価
* 自分の駒の動ける位置に１を入れた配列で行列計算させれば簡単かも...

* KK,KKPの行列を１つにしたい
	* 4次元配列からMat(5,12)のKK,KKPを取り出す
	* 盤面の数：12
	* 駒の数：5

# 盤面表現
* 行列の形で入力層に入れたい
| 行 | 内容 |
|---|---|
|0|ライオンの位置|
|1|ゾウの位置|
|2|キリンの位置|
|3|ニワトリの位置|
|4|ヒヨコの位置|
|5|持ち駒|

* 盤面の評価値のプラマイで考える
* 自分の駒は正、相手の駒は負
* minmax法で相手の次の手も考慮する
