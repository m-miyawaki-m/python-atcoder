import sys

input = sys.stdin.read
R = int(input().strip())

R_squared = R * R
count = 0

for i in range(-R, R + 1):
    # 円内に収まる場合のみ計算
    if (i + 0.5)**2 > R_squared:
        continue
    
    # 最大可能な j の範囲を計算
    max_j = int((R_squared - (i + 0.5)**2)**0.5)
    min_j = -max_j

    # 各 j を効率的にチェック
    for j in range(min_j, max_j + 1):
        # 各正方形の4頂点が円内に完全に収まるかを判定
        top_left = (i - 0.5)**2 + (j + 0.5)**2
        top_right = (i + 0.5)**2 + (j + 0.5)**2
        bottom_left = (i - 0.5)**2 + (j - 0.5)**2
        bottom_right = (i + 0.5)**2 + (j - 0.5)**2

        if top_left <= R_squared and top_right <= R_squared and bottom_left <= R_squared and bottom_right <= R_squared:
            count += 1

print(count)
