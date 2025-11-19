def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Разобьем индексы на категории по известности A_i и B_i:
    # 1) Оба известны (A_i != -1 и B_i != -1)
    # 2) A_i известен, B_i неизвестен
    # 3) A_i неизвестен, B_i известен
    # 4) Оба неизвестны

    known_sum = None  # фиксированная сумма S, если она однозначно определена

    # Сначала проверим индексы, где оба известны
    for i in range(N):
        if A[i] != -1 and B[i] != -1:
            s = A[i] + B[i]
            if known_sum is None:
                known_sum = s
            elif known_sum != s:
                print("No")
                return

    # Теперь рассмотрим индексы с одной известной частью
    # Для них сумма должна быть равна known_sum, если known_sum известна
    # Если known_sum неизвестна, то мы можем попытаться определить ее из этих индексов

    # Сначала соберем все возмож ограничения на сумму
    # Если есть хотя бы один индекс с обеими известными, known_sum уже определена

    # Если нет, попробуем определить known_sum из индексов с одной известной частью
    # Но для них known_sum может быть любое >= известной части (т.к. неизвестная часть можно подобрать)

    # Если known_sum не определена, то:
    # - Если есть индексы с одной известной частью, known_sum может быть любое >= max(известных частей)
    # - Если нет известных частей вообще, то known_sum может быть 0 (все -1, можно все заполнить нулями)

    # Соберем максимальное значение среди известных частей (A_i или B_i), чтобы known_sum >= max_known_part
    max_known_part = -1
    for i in range(N):
        if A[i] != -1:
            if A[i] > max_known_part:
                max_known_part = A[i]
        if B[i] != -1:
            if B[i] > max_known_part:
                max_known_part = B[i]

    # Если known_sum не определена, установим ее в max_known_part (минимально возможное)
    if known_sum is None:
        if max_known_part == -1:
            # Все -1, можно сделать все нулями, сумма 0
            print("Yes")
            return
        else:
            known_sum = max_known_part

    # Теперь проверим, что для каждого индекса можно подобрать A_i и B_i >=0,
    # чтобы A_i + B_i = known_sum, учитывая известные значения и возможность перестановки A.

    # Перестановка A позволяет нам менять порядок A_i, но не значения A_i, кроме замены -1.

    # Рассмотрим известные A_i != -1 и неизвестные (-1)
    # Аналогично для B_i

    # Для индексов с A_i != -1 и B_i != -1 мы уже проверили сумму

    # Для индексов с A_i != -1 и B_i == -1:
    # B_i = known_sum - A_i, должно быть >= 0 => known_sum >= A_i

    # Для индексов с A_i == -1 и B_i != -1:
    # A_i = known_sum - B_i, должно быть >= 0 => known_sum >= B_i

    # Для индексов с A_i == -1 и B_i == -1:
    # Можно выбрать A_i и B_i >=0, A_i + B_i = known_sum, всегда возможно

    # Проверим условия для всех индексов:

    for i in range(N):
        a = A[i]
        b = B[i]
        if a != -1 and b != -1:
            # уже проверено, сумма должна быть known_sum
            if a + b != known_sum:
                print("No")
                return
        elif a != -1 and b == -1:
            # b = known_sum - a >= 0
            if known_sum < a:
                print("No")
                return
        elif a == -1 and b != -1:
            # a = known_sum - b >= 0
            if known_sum < b:
                print("No")
                return
        else:
            # оба -1, всегда можно подобрать
            pass

    # Теперь учитываем перестановку A.
    # Перестановка A позволяет нам менять порядок A_i, но не значения A_i, кроме замены -1.

    # Важно: мы можем заменить все -1 в A на любые неотрицательные числа, и переставить A как угодно.

    # Значит, для индексов с A_i == -1, мы можем выбрать любые значения >=0.

    # Для индексов с A_i != -1, значения фиксированы.

    # Аналогично для B.

    # Мы уже проверили, что для каждого индекса можно подобрать B_i или A_i >=0.

    # Но нужно проверить, что существует перестановка A, чтобы для каждого i:
    # A_i + B_i = known_sum

    # Рассмотрим множества:

    # fixed_A = [a for a in A if a != -1]
    # unknown_A_count = количество -1 в A

    # fixed_B = [b for b in B if b != -1]
    # unknown_B_count = количество -1 в B

    # Для индексов с A_i != -1 и B_i == -1:
    # B_i = known_sum - A_i >=0

    # Для индексов с A_i == -1 и B_i != -1:
    # A_i = known_sum - B_i >=0

    # Для индексов с A_i == -1 и B_i == -1:
    # A_i + B_i = known_sum, можно подобрать любые неотрицательные

    # Перестановка A нужна, чтобы сопоставить fixed_A с B_i, чтобы все суммы были known_sum.

    # Но fixed_A значения фиксированы, а B_i могут быть известны или неизвестны.

    # Рассмотрим индексы с B_i != -1:

    # Для них A_i = known_sum - B_i >=0

    # Значит, для этих индексов, A_i должны быть равны known_sum - B_i.

    # Мы должны проверить, можно ли переставить fixed_A так, чтобы для все индексы с B_i != -1 и A_i != -1:

    # fixed_A содержит все значения known_sum - B_i для соответствующих индексов.

    # Аналогично, для индексов с A_i != -1 и B_i == -1:

    # B_i = known_sum - A_i >=0, B_i можно подобрать.

    # Для индексов с A_i == -1 и B_i == -1:

    # Можно подобрать любые A_i и B_i >=0, сумма known_sum.

    # Итого:

    # Для индексов с B_i != -1, A_i должны быть равны known_sum - B_i.

    # fixed_A содержит значения, которые мы можем переставить.

    # Проверим, что multiset fixed_A содержит multiset {known_sum - B_i | B_i != -1}

    # Если fixed_A не содержит нужных значений, то "No"

    # Для индексов с B_i == -1, A_i могут быть любыми >=0, в том числе и из unknown_A_count

    # Аналогично, unknown_A_count можно использовать для заполнения недостающих значений.

    from collections import Counter

    fixed_A = [a for a in A if a != -1]
    unknown_A_count = A.count(-1)

    fixed_B = [b for b in B if b != -1]
    unknown_B_count = B.count(-1)

    # Множество значений A_i, которые должны быть для индексов с B_i != -1:
    required_A_for_B = [known_sum - b for b in fixed_B]
    # Все должны быть >=0, проверено ранее

    count_fixed_A = Counter(fixed_A)
    count_required_A = Counter(required_A_for_B)

    # Проверим, что count_fixed_A покрывает count_required_A
    # Если count_required_A[x] > count_fixed_A[x], то недостает fixed_A с таким значением,
    # но мы можем использовать unknown_A_count для замены -1 в A на нужные значения.

    deficit = 0
    for val, cnt in count_required_A.items():
        have = count_fixed_A.get(val, 0)
        if have < cnt:
            deficit += cnt - have

    if deficit > unknown_A_count:
        # Недостаточно неизвестных A_i, чтобы покрыть требуемые значения
        print("No")
        return

    # Аналогично проверим для B:

    # Для индексов с A_i != -1, B_i = known_sum - A_i >=0

    # fixed_B должны покрывать known_sum - fixed_A

    required_B_for_A = [known_sum - a for a in fixed_A]
    count_fixed_B = Counter(fixed_B)
    count_required_B = Counter(required_B_for_A)

    deficit_B = 0
    for val, cnt in count_required_B.items():
        have = count_fixed_B.get(val, 0)
        if have < cnt:
            deficit_B += cnt - have

    if deficit_B > unknown_B_count:
        print("No")
        return

    # Если все проверки пройдены, ответ "Yes"
    print("Yes")


if __name__ == "__main__":
    main()