def calculate_dissatisfaction(N, L, R, P):
    total = 0
    for i in range(N):
        for j in range(N):
            if i != j and P[j] > P[i]:
                # Person j crosses seat P[i] at times L[j] and R[j]
                if L[i] < L[j] < R[i]:
                    total += 1
                if L[i] < R[j] < R[i]:
                    total += 1
    return total

def solve_case(N, L, R):
    # Try greedy approach: assign seats to minimize dissatisfaction
    # For lexicographically smallest, we want to assign person 1 to smallest possible seat
    
    best_dissatisfaction = float('inf')
    best_P = None
    
    # Use backtracking to find optimal assignment
    def backtrack(person, P, used_seats, current_dissatisfaction):
        nonlocal best_dissatisfaction, best_P
        
        if person == N:
            if current_dissatisfaction < best_dissatisfaction or \
               (current_dissatisfaction == best_dissatisfaction and (best_P is None or P < best_P)):
                best_dissatisfaction = current_dissatisfaction
                best_P = P[:]
            return
        
        # Prune if current dissatisfaction already exceeds best
        if current_dissatisfaction > best_dissatisfaction:
            return
        
        # Try assigning each available seat to current person
        for seat in range(1, N + 1):
            if seat in used_seats:
                continue
            
            # Calculate additional dissatisfaction from this assignment
            added_dissatisfaction = 0
            
            # Check how this person affects others already assigned
            for prev_person in range(person):
                prev_seat = P[prev_person]
                if seat > prev_seat:
                    # Current person crosses prev_person's seat
                    if L[prev_person] < L[person] < R[prev_person]:
                        added_dissatisfaction += 1
                    if L[prev_person] < R[person] < R[prev_person]:
                        added_dissatisfaction += 1
            
            # Check how already assigned people affect this person
            for prev_person in range(person):
                prev_seat = P[prev_person]
                if prev_seat > seat:
                    # Previous person crosses current person's seat
                    if L[person] < L[prev_person] < R[person]:
                        added_dissatisfaction += 1
                    if L[person] < R[prev_person] < R[person]:
                        added_dissatisfaction += 1
            
            P[person] = seat
            used_seats.add(seat)
            backtrack(person + 1, P, used_seats, current_dissatisfaction + added_dissatisfaction)
            used_seats.remove(seat)
    
    P = [0] * N
    used_seats = set()
    backtrack(0, P, used_seats, 0)
    
    return best_P

T = int(input())
for _ in range(T):
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    
    result = solve_case(N, L, R)
    print(' '.join(map(str, result)))