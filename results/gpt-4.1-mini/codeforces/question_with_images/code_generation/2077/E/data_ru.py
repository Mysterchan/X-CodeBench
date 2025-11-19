import sys
input = sys.stdin.readline

MOD = 998244353

# Анализ задачи:
# f(b) - минимальное количество операций для достижения конфигурации b.
# Операция: сгибание ленты и капание краски в одной точке, краска увеличивает темноту по пути вниз.
# После операции ленту разворачивают.
#
# Из условия и примеров можно вывести, что f(b) = max(b) - min(b).
# Почему?
# - Каждая операция увеличивает темноту некоторого подотрезка на 1.
# - Сгибания позволяют "наложить" несколько ячеек, чтобы увеличить их одновременно.
# - Минимальное число операций - это минимальное количество "слоёв" краски, чтобы получить все значения.
# - Так как краска увеличивает на 1, и можно накладывать ячейки, минимальное число операций равно разнице между максимальным и минимальным значением.
#
# Следовательно, для подмассива a[l..r]:
# f(a[l..r]) = max(a[l..r]) - min(a[l..r])
#
# Задача сводится к вычислению суммы по всем подотрезкам (max - min).
#
# Известная задача: сумма по всем подотрезкам разницы max и min.
# Решается с помощью монотонных стеков за O(n).
#
# Формула:
# sum_{l<=r} (max - min) = sum_{l<=r} max - sum_{l<=r} min
#
# Для вычисления sum_{l<=r} max:
# Для каждого элемента a[i] найдем количество подотрезков, где a[i] - максимальный элемент.
# Аналогично для min.
#
# Используем монотонные стеки:
# - Для max: стек по убыванию (чтобы найти границы, где a[i] - максимум)
# - Для min: стек по возрастанию
#
# Для каждого i:
# - left[i] - индекс ближайшего элемента слева, строго больше (для max) или строго меньше (для min)
# - right[i] - индекс ближайшего элемента справа, больше или меньше (в зависимости от max/min)
#
# Кол-во подотрезков, где a[i] - максимум: (i - left[i]) * (right[i] - i)
# Аналогично для min.
#
# Итог:
# sum_max = sum a[i] * (i - left_max[i]) * (right_max[i] - i)
# sum_min = sum a[i] * (i - left_min[i]) * (right_min[i] - i)
#
# Ответ = sum_max - sum_min по всем подотрезкам.
#
# Нужно посчитать это для каждого теста и вывести по модулю.

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Функция для вычисления суммы по подотрезкам, где a[i] - максимум
        def get_sum_max(arr):
            n = len(arr)
            left = [-1]*n
            right = [n]*n
            stack = []
            # Поиск left: ближайший элемент слева строго больше
            for i in range(n):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            stack.clear()
            # Поиск right: ближайший элемент справа строго больше или равен
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                right[i] = stack[-1] if stack else n
                stack.append(i)
            res = 0
            for i in range(n):
                res += arr[i] * (i - left[i]) * (right[i] - i)
            return res

        # Функция для вычисления суммы по подотрезкам, где a[i] - минимум
        def get_sum_min(arr):
            n = len(arr)
            left = [-1]*n
            right = [n]*n
            stack = []
            # Поиск left: ближайший элемент слева строго меньше
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            stack.clear()
            # Поиск right: ближайший элемент справа строго меньше или равен
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                right[i] = stack[-1] if stack else n
                stack.append(i)
            res = 0
            for i in range(n):
                res += arr[i] * (i - left[i]) * (right[i] - i)
            return res

        ans = (get_sum_max(a) - get_sum_min(a)) % MOD
        print(ans)

if __name__ == "__main__":
    solve()