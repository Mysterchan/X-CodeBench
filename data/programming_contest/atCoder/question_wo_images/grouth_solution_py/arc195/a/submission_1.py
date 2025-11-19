from functools import cache

def main(r):
	N,M=r.int
	A=r.intlist
	B=r.intlist

	f=True

	S1=[]
	bi=0
	for i,a in enumerate(A):
		if a==B[bi]:
			bi+=1
			S1.append(i)
		if not bi<len(B):
			break
	else:
		f=False

	if not f:
		print("No")
	else:
		S2=[]
		bi=len(B)-1
		for i,a in enumerate(A[::-1]):
			i=len(A)-i-1
			if a==B[bi]:
				bi-=1
				S2.append(i)
			if not 0<=bi:
				break

		pri()(S1!=S2[::-1])

def main0(r):
	N,M=r.int
	A=r.intlist
	B=r.intlist

	C = defaultdict(list)

	for i,e in enumerate(B[::-1]):
		C[e].append(len(B)-i-1)

	D = [0]*len(B)

	for a in A:
		for i in C[a]:
			if i==0:
				D[0]+=1
			else:
				D[i]+=D[i-1]

	pri()(2<=D[-1])

from types import SimpleNamespace as NS
from operator import itemgetter as iget
from functools import total_ordering,cmp_to_key,reduce,partial
from collections import deque,defaultdict,Counter
from itertools import count as cntiter,accumulate,islice,combinations,permutations,zip_longest,cycle,product,chain,groupby
import itertools;import random;import bisect;
import math;from statistics import mean;
import re;from textwrap import dedent;
import sys;sys.setrecursionlimit(300000)

from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import windowed,chunked,substrings

compare       = lambda a,b:"=" if a==b else ">" if a>b else "<"
LC,UC         = [chr(i) for i in range(97,123)],[chr(i) for i in range(65,91)]
is_palindrome = lambda S:S==S[::-1]
tx            = lambda txt:dedent(txt).strip()
pri           = lambda ok="Yes",ng="No": (lambda f:print(ok if f else ng))
prif          = lambda num:print(f"{num:.12f}")
nrange        = lambda n,step=1:range(1,n+1,step)
bitsearch     = lambda data:([e for i,e in enumerate(data) if pattern>>len(data)-1-i & 1] for pattern in range(2**len(data)))

bicount = {
    "<"  : lambda a,x: bisect.bisect_left(a, x),
    "<=" : lambda a,x: bisect.bisect_right(a, x),
    ">=" : lambda a,x: len(a) - bisect.bisect_left(a, x),
    ">"  : lambda a,x: len(a) - bisect.bisect_right(a, x),
}

def mkarr(*dim, val=0):
	if len((dim:=list(dim))) == 1:return [val for _ in range(dim[0])]
	return [mkarr(*dim[1:], val=val) for _ in range(dim[0])]

class Lstr:
	def __init__   (my,v=None):my._chars = list(str(v)) if v!=None else []
	def __str__    (my)       :return "".join(my._chars)
	def __getitem__(my,key)   :return "".join(my._chars[key]) if isinstance(key, slice) else my._chars[key]
	def __setitem__(my,i,val) :my._chars[i] = val
	def set        (my,i,val) :new = lstr(str(my));new[i]=val;return new
	def __iter__   (my)       :return iter(my._chars)

class RLE:
	def __init__(my,itr):
		my.l=[]
		prev,cnt=None,0
		for e in itr:
			if   cnt==0 :prev,cnt=e,1
			elif e==prev:cnt+=1
			else        :my.l.append((prev,cnt));prev,cnt=e,1
		if cnt:my.l.append((prev,cnt))
	def __str__(my):return str(my.l)
	def __len__(my):return len(my.l)
	def groups(my) :return ((k,v) for k,v in my.l)
	def expand(my) :return (k for k,v in my.l for _ in range(v))

class Que:
	from collections import deque
	def __init__(my,l=None):my.quelist = [] if l==None else l;my.quelist=my.deque(my.quelist)
	def pop     (my)       :return my.quelist.popleft()
	def push    (my,*e)    :[my.quelist.append(e2) for e2 in e]
	def poppush (my,e)     :my.push(e);return my.pop()
	def rotate  (my,n=1)   :my.quelist.rotate(-n)
	def __getitem__(my,key):return my.quelist[key]
	def __iter__(my)       :return iter(my.quelist)
	def __repr__(my)       :return str(list(my.quelist))
	def __len__ (my)       :return len(my.quelist)

class Heap:
	import heapq
	def __init__(my,l=None):my.heaplist = [] if l==None else l;my.heapq.heapify(my.heaplist)
	def pop     (my)       :return my.heapq.heappop(my.heaplist)
	def push    (my,e)     :my.heapq.heappush(my.heaplist,e)
	def __repr__(my)       :return str(my.heaplist)
	def __len__ (my)       :return len(my.heaplist)

class Val:
	def __init__(my,cmp,val=None):my.val,my.cmp,my.log,my.cnt,my.item = val,cmp,deque(maxlen=5),0,None
	def __str__ (my)             :return str(my.val)
	def update(my,*newval,item=None):
		if (F:=my.val==None):my.log.append(None);my.val=my.cmp(newval);
		elif (F:= my.val!=(V:=my.cmp(my.val,*newval))):my.log.append(my.val);my.val=V;my.cnt+=1
		if F:my.item=item
		return F

class Reader:
	from sys import stdin;P,rl=property,(lambda x:x.stdin.readline().rstrip())
	int       = P(lambda M: d[0] if len((d:=M.intlist))==1 else None if len(d)==0 else d)
	int_n     = lambda M,n:[M.int for _ in range(n)]
	intlist   = P(lambda M:[int(i) for i in M.rl().split()])
	intseq    = P(lambda M:(int(i) for i in M.rl().split()))
	intlist_n = lambda M,n:[M.intlist for _ in range(n)]
	str       = P(lambda M:(M.rl()))
	str_n     = lambda M,n:[M.str for _ in range(n)]
	strlist   = P(lambda M:M.rl().split())
	strlist_n = lambda M,n:[M.strlist for _ in range(n)]
	read      = lambda M,*tp:[T(v) for T,v in zip(tp,M.rl().split()) if T!=None]

if __name__=="__main__":
	main(Reader())