def max_items():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 入力のパース
    N = int(data[0])
    M = int(data[1])
    P = list(map(int, data[2:]))
    
    # 判定関数：x個の商品を購入できるか
    def can_buy(x):
        total_cost = 0
        for p in P:
            # 各商品の最大購入個数を計算
            if x == 0:
                continue
            k = int((x // p)**0.5)
            while k**2 * p > x:
                k -= 1
            while (k + 1)**2 * p <= x:
                k += 1
            total_cost += k**2 * p
            if total_cost > M:
                return False
        return total_cost <= M
    
    # 二分探索
    low, high = 0, 10**18
    while low < high:
        mid = (low + high + 1) // 2
        if can_buy(mid):
            low = mid
        else:
            high = mid - 1

    print(low)

