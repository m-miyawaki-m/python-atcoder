# 入力を取得
X = int(input())

# 初期化
N = 1
factorial = 1

# 階乗を累積的に計算しながら X と比較
while factorial < X:
    N += 1
    factorial *= N

# 結果を出力
print(N)