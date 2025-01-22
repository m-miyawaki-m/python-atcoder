# 入力の取得
N = int(input())
cake_size = list(map(int, input().split()))

# ポインタを初期化
small_index = 0  # 小さい餅を指すポインタ
large_index = N // 2  # 大きい餅を指すポインタ
pairs = 0  # 作成可能なペア数

# 2ポインタ法でペアを計算
while small_index < N // 2 and large_index < N:
    # 小さい餅が条件を満たす場合
    if cake_size[small_index] * 2 <= cake_size[large_index]:
        pairs += 1  # ペアを作成
        small_index += 1  # 小さい餅を次に進める
    # 常に大きい餅を次に進める
    large_index += 1

# 結果を出力
print(pairs)
