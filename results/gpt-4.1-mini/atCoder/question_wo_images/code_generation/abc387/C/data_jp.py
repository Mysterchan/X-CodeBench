def main():
    import sys
    sys.setrecursionlimit(10**7)
    L, R = map(int, sys.stdin.readline().split())

    # ヘビ数の定義：
    # 先頭の桁（最上位桁）が他のどの桁の数字よりも真に大きい
    # つまり、先頭の桁 > それ以外のすべての桁

    # 10以上なので桁数は2以上

    # 方針：
    # ある数N以下のヘビ数の個数を数える関数count(N)を作り、
    # 答えは count(R) - count(L-1)

    # count(N)はN以下のヘビ数の個数を返す

    # 先頭の桁d (1~9)
    # 残りの桁は長さlen-1
    # それらの桁はすべて dより小さい数字(0~d-1)で構成される

    # 先頭の桁は0にはならない
    # 先頭の桁はNの先頭桁以下でなければならない（N以下の制約）

    # DPで桁DPを行う
    # 状態：
    # pos: 現在の桁位置（0始まり、最上位桁から）
    # is_limit: これまでの桁がNの桁に一致しているか（Trueなら次の桁はNの桁以下）
    # is_num: すでに数字を置いたか（先頭桁を決めたか）
    # first_digit: 先頭の桁の値（決まっていなければ-1）
    #
    # 先頭桁を決めたら、それ以降の桁は0~first_digit-1の数字のみ許可
    #
    # 先頭桁は1~9
    #
    # 10以上なので、先頭桁は必ずpos=0で決まる

    from functools import lru_cache

    s = str(R)

    def count_up_to(num_str):
        n = len(num_str)

        @lru_cache(None)
        def dfs(pos, is_limit, is_num, first_digit):
            if pos == n:
                # 数字を置いていれば1、そうでなければ0
                return 1 if is_num else 0

            res = 0
            up = int(num_str[pos]) if is_limit else 9

            if not is_num:
                # まだ数字を置いていないなら、ここで置かない選択肢もあるが
                # 10以上なので先頭桁はpos=0で必ず置く必要がある
                # pos=0で数字を置かないのは無意味（0は10未満）
                # なのでpos=0でis_num=Falseなら数字を置た方が良い
                # ただしpos>0なら数字を置かない選択肢もある（先頭桁はすでに決まっている）
                # しかしヘビ数は10以上なので先頭桁はpos=0で必ず置く
                # ここではpos=0で数字を置た方が良いので、pos=0でis_num=Falseなら数字を置つ
                # pos>0でis_num=Falseはありえない（先頭桁はpos=0で決まる）
                # よってpos=0で数字を置た場合のみ考える
                # ただしpos=0で数字を置かない選択肢は0なのでスキップ
                pass

            # 数字を置く場合
            if not is_num:
                # 先頭桁を決める
                for d in range(1, up + 1):
                    # 先頭桁はd
                    # 次の桁は0~d-1の数字のみ許可
                    res += dfs(pos + 1, is_limit and (d == up), True, d)
            else:
                # 先頭桁はfirst_digitで決まっている
                # 次の桁は0~first_digit-1の数字のみ許可
                max_digit = min(up, first_digit - 1)
                for d in range(0, max_digit + 1):
                    res += dfs(pos + 1, is_limit and (d == up), True, first_digit)

            return res

        return dfs(0, True, False, -1)

    # L以上R以下のヘビ数の個数 = count(R) - count(L-1)
    # Lが10以上なのでL-1 >=9となるが9以下はヘビ数なしなので問題なし

    def dec_str(num_str):
        # num_strは数字文字列
        # 1引く
        num = list(map(int, num_str))
        i = len(num) - 1
        while i >= 0:
            if num[i] > 0:
                num[i] -= 1
                break
            else:
                num[i] = 9
                i -= 1
        # 先頭の0を除去
        while len(num) > 1 and num[0] == 0:
            num.pop(0)
        return ''.join(map(str, num))

    L_minus_1 = str(int(L) - 1) if L > 10 else "9"

    ans = count_up_to(str(R)) - count_up_to(L_minus_1)
    print(ans)


if __name__ == "__main__":
    main()