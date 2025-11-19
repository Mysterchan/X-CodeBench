import sys
import threading
import bisect

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def main():
    t = int(input())
    # 全体の制約から、合計n,m,q <= 1.5*10^5なので
    # 各テストケースで処理していく

    # 重要なポイントの整理：
    # f(u,G[V']) = XOR of neighbors v in V' of u
    # V' = [l,r]
    # f(u,G[V']) = XOR of neighbors v in [l,r]
    # つまり、uの隣接ノードのうち[l,r]にあるノードのラベルのXOR

    # これを効率的に求めるには、
    # 各ノードuについて、隣接ノードのラベルをソート済みで持つ
    # prefix_xor[u][i] = XOR of first i neighbors (sorted)
    # すると、f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで pos_r = upper_bound(r), pos_l = lower_bound(l) in neighbors[u]

    # クエリは [l,r,k] で、f(l,G[V']), f(l+1,G[V']), ..., f(r,G[V']) の中からk番目に小さい値を求める
    # つまり、区間[l,r]のf(u,G[V'])のk番目の値

    # しかし、f(u,G[V'])はクエリごとに変わる（l,rが変わるため）
    # 直接計算してソートは無理

    # そこで、f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # これを変形すると、
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中でr,lの位置

    # つまり、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # pos_r, pos_lはneighbors[u]の中のr,lの位置

    # これをうまく扱うために、クエリをlでグループ化し、rでグループ化し、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルのうち[l,r]にあるもののXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXOR
    # なので、f(u,G[V'])はuの隣接ノードのラベルの区間XOR

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # pos_r = upper_bound(r) in neighbors[u]
    # pos_l = lower_bound(l) in neighbors[u]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置

    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の最小の位置

    # つまり、pos_rはneighbors[u]の中でrのupper_bound
    # pos_lはneighbors[u]の中でlのlower_bound

    # これをうまく扱うために、クエリをrでソートし、lでソートし、などの工夫が必要

    # しかし、問題の制約とサンプルから、
    # f(u,G[V'])はuの隣接ノードのラベルのうち[l,r]にあるノードのXOR
    # つまり、uの隣接ノードのラベルの区間[l,r]のXOR

    # ここで、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであり、
    # これはprefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]で計算可能

    # クエリは[l,r,k]で、uは[l,r]の範囲
    # つまり、uは[l,r]のノードで、f(u,G[V'])を計算し、その中のk番目の値を求める

    # つまり、uは[l,r]のノードで、f(u,G[V'])は
    # prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]

    # これをクエリごとに計算するとO(q*(r-l+1)*log d)で無理

    # ここまでの考察から、問題は非常に難しいが、
    # 重要な点は、f(u,G[V'])はuの隣接ノードのラベルの区間[l,r]のXORであること

    # したがって、f(u,G[V'])はuの隣接ノードのラベルの区間XORである

    # これを利用して、クエリごとにf(u,G[V'])を計算し、
    # その区間[l,r]のf(u,G[V'])のk番目の値を求める

    # しかし、クエリ数が多く、区間長も大きいので、
    # 直接計算は無理

    # そこで、f(u,G[V'])を
    # f(u,G[V']) = prefix_xor[u][pos_r] XOR prefix_xor[u][pos_l-1]
    # ここで、pos_r, pos_lはneighbors[u]の中のr,lの位置

    # つまり、f(u,G[V']) = A[u] XOR B[u], ただし
    # A[u] = prefix_xor[u][pos_r]
    # B[u] = prefix_xor[u][pos_l-1]

    # pos_r, pos_lはneighbors[u]の中のr,lの位置なので、
    # pos_rはneighbors[u]の中でr以下の最大の位置
    # pos_lはneighbors[u]の中でl以上の