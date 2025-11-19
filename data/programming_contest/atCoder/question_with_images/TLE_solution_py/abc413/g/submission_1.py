from __future__ import annotations
from functools import reduce
from itertools import *
from collections import defaultdict
from typing import Optional, List, Tuple, Dict

def read_int() -> int:
	return int(input())

def read_tuple() -> tuple[int, ...]:
	return tuple(map(int, input().split()))

def read_list() -> list[int]:
	return list(map(int, input().split()))

def YesNo(b: bool) -> str:
	return 'Yes' if b else 'No'

class UnionFind:
	def __init__(self, N: int) -> None:
		self.parents: list[int] = list(range(N))
		self.heights: list[int] = [1] * N

	def connect(self, v1: int, v2: int) -> None:
		r1 = self.root(v1)
		r2 = self.root(v2)
		if r1 == r2:
			return

		h1 = self.heights[r1]
		h2 = self.heights[r2]
		if h1 <= h2:
			self.parents[r1] = r2
			self.heights[r2] = max(self.heights[r2], self.heights[r1]+1)
		else:
			self.parents[r2] = r1
			self.heights[r1] = max(self.heights[r1], self.heights[r2]+1)

	def root(self, v: int) -> int:
		while self.parents[v] != v:
			v = self.parents[v]
		return v

Point = Tuple[int, int]
Range = Tuple[int, int]
Boundary = List[Tuple[Range, int]]

class Cell:
	def __init__(self, x1: int, x2: int, y1: int, y2: int,
											objs: list[Point]) -> None:
		self.x1: int = x1
		self.x2: int = x2
		self.y1: int = y1
		self.y2: int = y2
		self.objects: list[Point] = objs
		if len(objs) == 1:
			x, y = objs[0]
			if x2 - x1 == 1:
				if y2 - y1 == 1:
					self.left: list[tuple[Point, int]] = []
					self.bottom: list[tuple[Point, int]] = []
					self.right: list[tuple[Point, int]] = []
					self.top: list[tuple[Point, int]] = []
				elif y == y1:
					self.left = []
					self.bottom = [((y1+1, y2), 0)]
					self.right = [((x1, x2), 0)]
					self.top = [((y1+1, y2), 0)]
				elif y == y2 - 1:
					self.left = [((x1, x2), 0)]
					self.bottom = [((y1, y2-1), 0)]
					self.right = []
					self.top = [((y1, y2-1), 0)]
				else:
					self.left = [((x1, x2), 0)]
					self.bottom = [((y1, y), 0), ((y+1, y2), 1)]
					self.right = [((x1, x2), 1)]
					self.top = [((y1, y), 0), ((y+1, y2), 1)]
			elif y2 - y1 == 1:
				if x == x1:
					self.left = [((x1+1, x2), 0)]
					self.bottom = [((y1, y2), 0)]
					self.right = [((x1+1, x2), 0)]
					self.top = []
				elif x == x2 - 1:
					self.left = [((x1, x2-1), 0)]
					self.bottom = []
					self.right = [((x1, x2-1), 0)]
					self.top = [((y1, y2), 0)]
				else:
					self.left = [((x1, x), 0), ((x+1, x2), 1)]
					self.bottom = [((y1, y2), 1)]
					self.right = [((x1, x), 0), ((x+1, x2), 1)]
					self.top = [((y1, y2), 0)]
			else:
				if y == y1:
					self.left = []
					if x > x1:
						self.left.append(((x1, x), 0))
					if x < x2 - 1:
						self.left.append(((x+1, x2), 0))
					self.right = [((x1, x2), 0)]
				elif y == y2 - 1:
					self.left = [((x1, x2), 0)]
					self.right = []
					if x > x1:
						self.right.append(((x1, x), 0))
					if x < x2 - 1:
						self.right.append(((x+1, x2), 0))
				else:
					self.left = [((x1, x2), 0)]
					self.right = [((x1, x2), 0)]

				if x == x1:
					self.top = []
					if y > y1:
						self.top.append(((y1, y), 0))
					if y < y2 - 1:
						self.top.append(((y+1, y2), 0))
					self.bottom = [((y1, y2), 0)]
				elif x == x2 - 1:
					self.top = [((y1, y2), 0)]
					self.bottom = []
					if y > y1:
						self.bottom.append(((y1, y), 0))
					if y < y2 - 1:
						self.bottom.append(((y+1, y2), 0))
				else:
					self.top = [((y1, y2), 0)]
					self.bottom = [((y1, y2), 0)]
		else:
			min_x = min(x for x, y in objs)
			max_x = max(x for x, y in objs)
			min_y = min(y for x, y in objs)
			max_y = max(y for x, y in objs)
			if max_x - min_x >= max_y - min_y:
				objs.sort(key=lambda obj: obj[0])
				mid = len(objs) // 2
				if objs[0][0] == objs[mid][0]:
					x = objs[mid][0] + 1
				else:
					x = objs[mid][0]
				objs1 = [ obj for obj in objs if obj[0] < x ]
				objs2 = [ obj for obj in objs if obj[0] >= x ]
				cell1 = Cell(x1, x, y1, y2, objs1)
				cell2 = Cell(x, x2, y1, y2, objs2)
			else:
				objs.sort(key=lambda obj: obj[1])
				mid = len(objs) // 2
				if objs[0][1] == objs[mid][1]:
					y = objs[mid][1] + 1
				else:
					y = objs[mid][1]
				objs1 = [ obj for obj in objs if obj[1] < y ]
				objs2 = [ obj for obj in objs if obj[1] >= y ]
				cell1 = Cell(x1, x2, y1, y, objs1)
				cell2 = Cell(x1, x2, y, y2, objs2)
			v = Cell.merge(cell1, cell2)
			self.left = v[0]
			self.bottom = v[1]
			self.right = v[2]
			self.top = v[3]

	def boundaries(self) -> list[Boundary]:
		return [self.left, self.bottom, self.right, self.top]

	def num_groups(self) -> int:
		max_g = -1
		for b in self.boundaries():
			for _, g in b:
				max_g = max(max_g, g)
		return max_g + 1

	@staticmethod
	def normalize(b: Boundary, uf: UnionFind) -> Boundary:
		new_b = []
		for g, v in groupby(b, key=lambda e: uf.root(e[1])):
			w = list(v)
			first = w[0][0][0]
			last = w[-1][0][1]
			new_b.append(((first, last), g))
		return new_b

	@staticmethod
	def merge_core(b1: Boundary, b2: Boundary,
							ng: int, uf: UnionFind) -> None:
		k, l = 0, 0
		L1, L2 = len(b1), len(b2)
		while k < L1 and l < L2:
			(first1, last1), g1 = b1[k]
			(first2, last2), g2 = b2[l]
			first = max(first1, first2)
			last = min(last1, last2)
			if first < last:
				uf.connect(g1, g2 + ng)
			if last1 <= last2:
				k += 1
			if last1 >= last2:
				l += 1

	@staticmethod
	def merge_each(b1: Boundary, b2: Boundary,
							dic: dict[int, int], ng1: int) -> Boundary:
		b1 = Cell.convert(b1, dic, 0)
		b2 = Cell.convert(b2, dic, ng1)
		if b1 and b2 and b1[-1][1] == b2[0][1] and b1[-1][0][1] == b2[0][0][0]:
			b = b1[:-1]
			rng1, g1 = b1[-1]
			rng2, g2 = b2[0]
			rng = (rng1[0], rng2[1])
			b.append((rng, g1))
			b.extend(b2[1:])
			return b
		else:
			return b1 + b2

	@staticmethod
	def convert(b: Boundary, dic: dict[int, int], d: int) -> Boundary:
		return [ (rng, dic[g+d]) for rng, g in b ]

	@staticmethod
	def merge(c1: Cell, c2: Cell) -> list[list[tuple[Range, int]]]:
		ng1 = c1.num_groups()
		ng2 = c2.num_groups()
		uf = UnionFind(ng1 + ng2)
		if c1.x2 == c2.x1:
			Cell.merge_core(c1.bottom, c2.top, ng1, uf)
		else:
			Cell.merge_core(c1.right, c2.left, ng1, uf)

		dic: dict[int, list[int]] = defaultdict(list)
		for i in range(ng1 + ng2):
			r = uf.root(i)
			dic[r].append(i)

		dic2: dict[int, int] = { }
		for i, vs in enumerate(dic.values()):
			for v in vs:
				dic2[v] = i

		if c1.x2 == c2.x1:
			left = Cell.merge_each(c1.left, c2.left, dic2, ng1)
			bottom = Cell.convert(c2.bottom, dic2, ng1)
			right = Cell.merge_each(c1.right, c2.right, dic2, ng1)
			top = Cell.convert(c1.top, dic2, 0)
		else:
			left = Cell.convert(c1.left, dic2, 0)
			bottom = Cell.merge_each(c1.bottom, c2.bottom, dic2, ng1)
			right = Cell.convert(c2.right, dic2, ng1)
			top = Cell.merge_each(c1.top, c2.top, dic2, ng1)
		return [left, bottom, right, top]

def read_input() -> tuple[int, int, list[Point]]:
	H, W, K = read_tuple()
	objs: list[Point] = []
	for _ in range(K):
		x, y = read_tuple()
		objs.append((x - 1, y - 1))
	return (H, W, objs)

def F(H: int, W: int, objs: list[Point]) -> bool:
	if not objs:
		return True

	c = Cell(0, H, 0, W, objs)
	if not c.left:
		return False
	else:
		rng1, g1 = c.left[0]
		if rng1[0] != 0:
			return False
	if not c.right:
		return False
	else:
		rng2, g2 = c.right[-1]
		if rng2[1] != H:
			return False

	return g1 == g2

H, W, objs = read_input()
print(YesNo(F(H, W, objs)))