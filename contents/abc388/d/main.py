# 入力の取得
N = int(input())
A = list(map(int, input().split()))

# 最終的な所持石を格納する配列
B = A[:]  # 初期値をコピー

# 成人祝いを管理する配列
distribution = [0] * (N + 1)

# 成人祝いのシミュレーション
for i in range(N):
    # 現時点の石を反映
    B[i] += distribution[i]

    # 成人祝いの分配
    give = B[i]
    if give > 0:
        B[i] -= give
        # 次の成人に配布範囲を設定
        if i + 1 < N:
            distribution[i + 1] += give
        if i + give + 1 < N:
            distribution[i + give + 1] -= give

# 分配結果を累積計算
current = 0
for i in range(N):
    current += distribution[i]
    B[i] += current

# 結果を出力
print(' '.join(map(str, B)))
