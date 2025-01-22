# 入力を取得
N, D = map(int, input().split())
snakes = [tuple(map(int, input().split())) for _ in range(N)]

# 各 k(1≤k≤D) について計算
for k in range(1, D + 1):
    # 各ヘビの長さが k 伸びたときの重さを計算
    weights = [(T * (L + k)) for T, L in snakes]
    # 最大の重さを出力
    print(max(weights))