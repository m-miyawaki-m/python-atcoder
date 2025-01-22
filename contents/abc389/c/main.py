def snake_queue():
    """
    ヘビの待ち行列をシミュレートする関数 (仕様準拠＋効率化＋デバッグ付き)

    標準入力から入力を読み込みます。

    Returns:
      タイプ3のクエリの出力結果のリスト
    """
    Q = int(input())  # クエリの数
    queries = []  # クエリのリスト

    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)

    queue = []  # 各ヘビの累積和 (頭位置、長さ) を格納
    shift = 0  # 現在の全体座標のシフト量
    results = []  # タイプ3のクエリの出力結果を格納

    def debug_log(step, query, queue, shift, results):
        """デバッグ用のログ出力"""
        print(f"Step {step}: Query = {query}")
        print(f"  Queue: {queue}")
        print(f"  Shift: {shift}")
        print(f"  Results: {results}")
        print("-" * 40)

    for step, query in enumerate(queries, start=1):
        query_type = query[0]

        if query_type == 1:  # ヘビの追加
            length = query[1]
            # 新しいヘビの頭位置を計算
            if queue:
                head_position = queue[-1][0] + queue[-1][1]
            else:
                head_position = 0
            queue.append((head_position, length))

        elif query_type == 2:  # ヘビの削除
            # 先頭のヘビを削除し、全体のシフトを更新
            removed_head, removed_length = queue.pop(0)
            shift += removed_length

        elif query_type == 3:  # ヘビの位置出力
            k = query[1]
            # k番目のヘビの現在の頭位置を計算
            head_position = queue[k - 1][0] - shift
            results.append(head_position)

        # デバッグログを出力
        debug_log(step, query, queue, shift, results)

    return results

# 関数の実行
results = snake_queue()

# 出力
if results:
    for result in results:
        print(result)
else:
    print()
