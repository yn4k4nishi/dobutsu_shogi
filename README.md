# 遺伝的アルゴリズム
* KKP,KKを採用

#盤面評価について
* 相手と自分のライオンの位置で予め持っていいるKK,KKP(遺伝子)で盤面を評価
* 自分の駒の動ける位置に１を入れた配列で行列計算させれば簡単かも...

* KK,KKPの行列を１つにしたい
	* 4次元配列からMat(5,12)のKK,KKPを取り出す
	* 盤面の数：12
	* 駒の数：5
