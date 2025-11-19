import sys
import threading

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        sumA = sumB = sumC = sumD = sumE = 0
        res = []
        for _ in range(n):
            a = int(next(it)); b = int(next(it))
            c = int(next(it)); d = int(next(it))
            e = int(next(it))
            sumA += a
            sumB += b
            sumC += c
            sumD += d
            sumE += e
            # Each contest needs: 1 A, 2 B (Div1+Div2), 3 C (all three divisions),
            # 2 D (Div2+Div3), 1 E per contest.
            # So max contests = min(sumA, sumE, sumB//2, sumD//2, sumC//3)
            x = sumA
            if sumE < x: x = sumE
            b2 = sumB // 2
            if b2 < x: x = b2
            d2 = sumD // 2
            if d2 < x: x = d2
            c3 = sumC // 3
            if c3 < x: x = c3
            res.append(str(x))
        out.append(" ".join(res))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()