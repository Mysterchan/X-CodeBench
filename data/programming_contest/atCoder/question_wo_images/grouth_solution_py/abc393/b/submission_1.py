S = input()
cnt = 0
if "A" in S and "B" in S and "C" in S:
    read_A = 0
    while read_A < len(S):

        if S[read_A] == "A":
            read_B = read_A + 1
            while read_B < len(S):

                if S[read_B] == "B":
                    distance = read_B - read_A
                    target_idx = read_B + distance
                    if target_idx < len(S):
                        if S[target_idx] == "C":
                            cnt += 1
                read_B += 1
        read_A += 1

print(cnt)