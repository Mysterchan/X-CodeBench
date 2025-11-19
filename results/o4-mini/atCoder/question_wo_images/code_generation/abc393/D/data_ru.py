import sys
import threading

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    
    # Собираем позиции единиц (1-based indexing)
    pos = []
    for i, ch in enumerate(s):
        if ch == '1':
            pos.append(i + 1)
    
    k = len(pos)
    # Строим массив a_i = pos[i] - i (i from 0 to k-1)
    a = [pos[i] - i for i in range(k)]
    
    # Выбираем медиану
    m = k // 2
    median = a[m]
    
    # Считаем сумму абсолютных отклонений
    ans = 0
    for x in a:
        ans += abs(x - median)
    
    print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()