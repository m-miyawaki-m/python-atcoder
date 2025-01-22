import bisect

# 入力を取得
N = int(input())
A = list(map(int, input().split()))

# 鏡餅の種類数をカウント
count = 0

# 上に乗せる餅 A[i] を固定し、条件を満たす餅 A[j] を探索
for i in range(N):
    max_a = A[i] // 2
    idx = bisect.bisect_right(A, max_a, 0, i)  # 範囲を [0, i) に限定して探索
    count += idx

# 結果を出力
print(count)