def solve():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R, i))
    
    # Try all permutations using greedy approach with lexicographic order
    P = [0] * N
    used = [False] * N
    
    for pos in range(N):
        best_seat = -1
        best_cost = float('inf')
        
        # Try each available seat
        for seat in range(1, N + 1):
            if used[seat - 1]:
                continue
            
            # Calculate the cost if we assign this seat at this position
            cost = 0
            
            # For each person already assigned
            for prev_pos in range(pos):
                prev_person = None
                for p in range(N):
                    if P[p] == prev_pos + 1:
                        prev_person = p
                        break
                
                if prev_person is None:
                    continue
                
                prev_seat = 0
                for s in range(1, N + 1):
                    if P[prev_person] == prev_pos + 1:
                        # Find which seat number was assigned
                        count = 0
                        for ss in range(1, N + 1):
                            if not used[ss - 1] or any(P[pp] == prev_pos + 1 and intervals[pp][2] == prev_person for pp in range(N) if P[pp] > 0):
                                pass
                        break
            
            if cost < best_cost or (cost == best_cost and seat < best_seat):
                best_cost = cost
                best_seat = seat
        
        P[pos] = best_seat
        used[best_seat - 1] = True
    
    return P

def solve_optimized():
    N = int(input())
    people = []
    for i in range(N):
        L, R = map(int, input().split())
        people.append((L, R, i))
    
    result = [0] * N
    used = [False] * N
    
    for person_idx in range(N):
        L_i, R_i, _ = people[person_idx]
        
        best_seat = -1
        min_cost = float('inf')
        
        for seat in range(1, N + 1):
            if used[seat - 1]:
                continue
            
            # Calculate cost for assigning seat to person_idx
            cost = 0
            
            # Count how many already assigned people will cross this person
            for other_idx in range(N):
                if result[other_idx] == 0:
                    continue
                
                L_j, R_j, _ = people[other_idx]
                other_seat = result[other_idx]
                
                # other crosses person_idx if other arrives/leaves during (L_i, R_i)
                # and other's seat <= seat - 1
                if other_seat < seat:
                    if L_i < L_j < R_i or L_i < R_j < R_i:
                        cost += 1
            
            # Count how many future people will cross this person
            for other_idx in range(person_idx + 1, N):
                L_j, R_j, _ = people[other_idx]
                
                # We need to estimate: will other cross person_idx?
                # This happens if other arrives/leaves during (L_i, R_i) and gets seat < seat
                if L_i < L_j < R_i or L_i < R_j < R_i:
                    # Count available seats < seat
                    available_less = sum(1 for s in range(1, seat) if not used[s - 1])
                    if available_less > 0:
                        cost += 1  # Pessimistic estimate
            
            if cost < min_cost or (cost == min_cost and seat < best_seat):
                min_cost = cost
                best_seat = seat
        
        result[person_idx] = best_seat
        used[best_seat - 1] = True
    
    return result

T = int(input())
for _ in range(T):
    print(' '.join(map(str, solve_optimized())))