def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Bと一致する部分列を2つ以上見つける
    # 貪欲法で最初の一致を見つけ、次に2番目の一致を探す
    
    def find_subsequence(start_idx, used_indices=None):
        """
        start_idxから始めてBと一致する部分列を見つける
        used_indicesがある場合、それらのインデックスを避ける
        一致する部分列のインデックスリストを返す。見つからない場合はNone
        """
        if used_indices is None:
            used_indices = set()
        
        indices = []
        a_idx = start_idx
        b_idx = 0
        
        while a_idx < N and b_idx < M:
            if a_idx not in used_indices and A[a_idx] == B[b_idx]:
                indices.append(a_idx)
                b_idx += 1
            a_idx += 1
        
        if b_idx == M:
            return indices
        return None
    
    # 最初の一致を見つける
    first_match = find_subsequence(0)
    
    if first_match is None:
        print("No")
        return
    
    # 2つ目の一致を探す
    # 最初の一致の各インデックスについて、それを使わずに一致を探す
    for skip_idx in range(len(first_match)):
        # skip_idxの位置のインデックスを使わずに一致を探す
        indices = []
        a_idx = 0
        b_idx = 0
        
        while a_idx < N and b_idx < M:
            # skip_idxの位置では、first_match[skip_idx]を使わない
            if b_idx == skip_idx:
                # この位置では、first_match[skip_idx]以外で一致するものを探す
                if A[a_idx] == B[b_idx] and a_idx != first_match[skip_idx]:
                    indices.append(a_idx)
                    b_idx += 1
                    a_idx += 1
                else:
                    a_idx += 1
            else:
                if A[a_idx] == B[b_idx]:
                    indices.append(a_idx)
                    b_idx += 1
                    a_idx += 1
                else:
                    a_idx += 1
        
        if b_idx == M and indices != first_match:
            print("Yes")
            return
    
    print("No")

solve()