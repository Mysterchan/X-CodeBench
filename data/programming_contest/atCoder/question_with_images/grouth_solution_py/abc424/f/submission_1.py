#!/usr/bin/env python3
from sys import maxsize, stdin

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))

def dprint(*args, pretty=True):
    def _inner(v):
        def _dim(v): return (1 + min(_dim(x) for x in v) if v else 1) if isinstance(v, (list, tuple)) else 1 if isinstance(v, str) and len(v) > 1 else 0
        def _format_2d(v): return '\n' + '\n'.join([' '.join([str(y) for y in x]) for x in v])
        def _format_3d(v): return '\n' + '\n'.join(['\n'.join([' '.join([str(z) for z in y]) for y in x]) + '\n' for x in v]).rstrip('\n')
        dim = _dim(v) if pretty else -1
        return _format_3d(v) if dim == 3 else _format_2d(v) if dim == 2 else str(v)
    from ast import Call, parse, unparse, walk
    from inspect import currentframe, getsourcelines
    frame = currentframe().f_back
    source_lines, start_line = getsourcelines(frame)
    tree = parse(source_lines[frame.f_lineno - max(1, start_line)].strip())
    call_node = next(node for node in walk(tree) if isinstance(node, Call) and node.func.id == 'dprint')
    arg_names = [unparse(arg) for arg in call_node.args]
    print(', '.join([f'\033[4;35m{name}:\033[0m {_inner(value)}' for name, value in zip(arg_names, args)]))

class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            p >>= 1
            self._d[p] = self._op(self._d[p << 1], self._d[p << 1 | 1])

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, s, e):

        sml, smr = self._e(), self._e()
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                sml = self._op(sml, self._d[s])
                s += 1
            if e & 1:
                e -= 1
                smr = self._op(self._d[e], smr)
            s >>= 1
            e >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def update(self, p, x, func):
        y = self.get(p)
        self.set(p, func(x, y))

def main():
    n, q = iread(), iread()
    INF = maxsize
    def op0(x, y): return max(x, y)
    def e0(): return -INF
    st0 = SegTree(op0, e0, n + 5)
    def op1(x, y): return min(x, y)
    def e1(): return INF
    st1 = SegTree(op1, e1, n + 5)
    ans = []
    for _ in range(q):
        a, b = iread() - 1, iread() - 1
        v = st0.prod(a, b + 1)
        if v > b:
            ans.append('No')
            continue
        v = st1.prod(a, b + 1)
        if v < a:
            ans.append('No')
            continue
        ans.append('Yes')
        st0.set(a, b)
        st1.set(b, a)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()