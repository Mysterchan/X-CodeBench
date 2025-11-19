from sys import stdin

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

class UnionFind:
    def __init__(self, n):
        self._n = n
        self._root_or_size = [-1 for _ in range(n)]
        self._count = n

    def find(self, i):
        if self._root_or_size[i] < 0:
            return i
        self._root_or_size[i] = self.find(self._root_or_size[i])
        return self._root_or_size[i]

    def unite(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return ri
        self._count -= 1
        if -self._root_or_size[ri] < -self._root_or_size[rj]:
            ri, rj = rj, ri
        self._root_or_size[ri] += self._root_or_size[rj]
        self._root_or_size[rj] = ri
        return ri

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def size(self, i):
        return -self._root_or_size[self.find(i)]

    def groups(self):
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[self.find(i)].append(i)
        return [x for x in result if x]

    def count(self):
        return self._count

def main():
    h, w, k = iread(), iread(), iread()
    rc = [(iread(), iread()) for _ in range(k)]
    uf = UnionFind(k)
    d = {}
    for i, (r, c) in enumerate(rc):
        d[(r, c)] = i
    for i, (r, c) in enumerate(rc):
        for vi, vj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            ni, nj = r + vi, c + vj
            if (ni, nj) in d:
                uf.unite(i, d[(ni, nj)])
    for p in uf.groups():
        f0, f1 = False, False
        for k in p:
            i, j = rc[k]
            if i == 1 or j == w:
                f0 = True
            if i == h or j == 0:
                f1 = True
        if f0 and f1:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()