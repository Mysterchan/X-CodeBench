from sys import stdout
import bisect
import builtins
import math
import os
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from io import BytesIO, IOBase, StringIO

BUFSIZE = 1 << 20


class FastIO(IOBase):
    def __init__(self, fd):
        self._fd = fd
        self.buffer = BytesIO()
        self.writable = fd == 1
        self.ptr = 0

    def read(self):
        while True:
            b = os.read(self._fd, BUFSIZE)
            if not b:
                break
            self.buffer.seek(0, 2), self.buffer.write(b)
        return self.buffer.getvalue()

    def readline(self):
        while True:
            i = self.buffer.getvalue().find(b"\n", self.ptr)
            if i >= 0:
                i += 1
                line = self.buffer.getvalue()[self.ptr : i]
                self.ptr = i
                return line
            b = os.read(self._fd, BUFSIZE)
            if not b:
                line = self.buffer.getvalue()[self.ptr :]
                self.ptr = len(self.buffer.getvalue())
                return line
            self.buffer.seek(0, 2), self.buffer.write(b)

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, fd):
        self.buffer = FastIO(fd)
        self.read = lambda: self.buffer.read().decode()
        self.readline = lambda: self.buffer.readline().decode()
        self.write = lambda s: self.buffer.buffer.write(s.encode())
        self.flush = self.buffer.flush


sys.stdin, _ = IOWrapper(0), IOWrapper(1)
def input():
    return sys.stdin.readline().rstrip("\n")
def print(*args, sep=' ', end='\n', flush=False):
    s = sep.join(map(str, args)) + end
    sys.stdout.write(s)
    if flush:
        sys.stdout.flush()
mod = 998244353

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = [[] for _ in range(n+1)]
        degree = [0 for _ in range(n+1)]
        maxDegree = 0
        maxDegreeEle = -1
        for _ in range(n-1):
            u,v = map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
            if degree[u]>maxDegree:
                maxDegree=degree[u]
                maxDegreeEle=u
            if degree[v]>maxDegree:
                maxDegree=degree[v]
                maxDegreeEle=v
        queue = deque()
        res = int(1e9)
        for i in range(n+1):
            if degree[i]==maxDegree:
                queue.append((i,0))
                visit = set()
                count = 0
                while queue:
                    ele,dis = queue.popleft()
                    if ele in visit:
                        continue
                    if degree[ele]==1 and dis>1:
                        count+=1
                    for neg in graph[ele]:
                        if neg not in visit:
                            queue.append((neg,dis+1))
                    visit.add(ele)
                res=min(res,count)
        print(res)



if __name__ == "__main__":
    main()
