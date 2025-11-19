t = int(input())

for _ in range(t):
    s, k = map(int, input().split())
    
    # The maximum power Gleb can have at the end is determined by the distance he needs to cover
    # and the initial power he has.
    # If he can reach the end without turning, he will have k - (s - k) power left.
    # If he needs to turn, he will lose power for each turn.
    
    # The maximum power he can have is the maximum of 0 and k - (s - k)
    # This is because if he has to turn, he will lose power.
    
    max_power = max(0, k - (s - k))
    
    print(max_power)