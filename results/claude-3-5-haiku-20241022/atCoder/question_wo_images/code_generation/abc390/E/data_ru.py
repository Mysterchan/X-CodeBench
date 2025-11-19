N, X = map(int, input().split())
foods = []
for _ in range(N):
    v, a, c = map(int, input().split())
    foods.append((v, a, c))

# Разделяем продукты по типам витаминов
vit = [[], [], []]
for v, a, c in foods:
    vit[v-1].append((a, c))

# Для каждого типа витамина создаем список возможных комбинаций (витамины, калории)
def get_combinations(items):
    # dp[cal] = максимальное количество витаминов при использовании cal калорий
    dp = {}
    dp[0] = 0
    
    for amount, calories in items:
        new_dp = dp.copy()
        for cal, val in dp.items():
            new_cal = cal + calories
            if new_cal <= X:
                new_dp[new_cal] = max(new_dp.get(new_cal, 0), val + amount)
        dp = new_dp
    
    return dp

# Получаем комбинации для каждого витамина
combs = []
for i in range(3):
    combs.append(get_combinations(vit[i]))

# Преобразуем в списки для удобства
lists = []
for i in range(3):
    lst = [(cal, val) for cal, val in combs[i].items()]
    lst.sort()
    lists.append(lst)

answer = 0

# Перебираем все комбинации для витаминов 1, 2, 3
for cal1, val1 in lists[0]:
    for cal2, val2 in lists[1]:
        if cal1 + cal2 > X:
            break
        remaining = X - cal1 - cal2
        
        # Находим максимальное значение витамина 3 при оставшихся калориях
        for cal3, val3 in lists[2]:
            if cal3 <= remaining:
                min_val = min(val1, val2, val3)
                answer = max(answer, min_val)

print(answer)