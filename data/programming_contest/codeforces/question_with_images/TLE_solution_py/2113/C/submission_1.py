import os
import sys
from io import BytesIO, IOBase

def II():
    return int(input())
def IS():
    return input().split()
def MI():
    return map(int,input().split())
def LI():
    return list(map(int,input().split()))

def minpow2finder(x,y):
    if x>y:return -1
    p=0
    while (1<<p)<x:p+=1
    c=1<<p
    if c<=y:
        return c
    return -1
def destruct(empty,gold,k):
    e1,e2=empty
    g1,g2=gold
    return (abs(g1-e1)<k and abs(g2-e2)<k)
def main():
    t = II()
    for _ in range(t):
        n,m,k=MI()
        g=set()
        gtot=0
        e=set()
        for r in range(n):
            row=input()
            for c in range(m):
                block=row[c]
                if block=='g':
                    g.add((r,c))
                    gtot+=1
                elif block=='.':
                    e.add((r,c))
        minloss=250000
        for empty in e:
            loss=0
            for gold in g:
                if destruct(empty,gold,k):
                    loss+=1
            if loss<minloss:
                minloss=loss
        print(gtot-minloss)


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()
