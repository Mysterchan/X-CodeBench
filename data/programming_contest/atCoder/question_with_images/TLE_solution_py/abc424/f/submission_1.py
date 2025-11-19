import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class SegmentTree:
    def __init__(self, numEle, funcBinaryOperation, idEle):
        self.funcBinaryOperation = funcBinaryOperation
        self.idEle = idEle
        self.makeSegmentTree(numEle)
    def makeSegmentTree(self, numEle):
        self.numEle = numEle
        self.logNum = (self.numEle-1).bit_length()
        self.numPow2 = 1 << self.logNum
        self.data = [self.idEle for _ in range(2*self.numPow2)]
    def setInit(self, As):
        for iST, A in enumerate(As, self.numPow2):
            self.data[iST] = A
        for iST in reversed(range(1, self.numPow2)):
            self._recalc(iST)
    def _recalc(self, iST):
        self.data[iST] = self.funcBinaryOperation(self.data[2*iST], self.data[2*iST+1])
    def add1(self, iA, A):
        iST = iA + self.numPow2
        self.data[iST] += A
        for d in range(1, self.logNum+1):
            self._recalc(iST >> d)
    def set1(self, iA, A):
        iST = iA + self.numPow2
        self.data[iST] = A
        for d in range(1, self.logNum+1):
            self._recalc(iST >> d)
    def update1(self, iA, A):
        iST = iA + self.numPow2
        self.data[iST] = A
        for d in range(1, self.logNum+1):
            self._recalc(iST >> d)
    def getRange(self, iFr, iTo):
        L = iFr + self.numPow2
        R = iTo + self.numPow2
        ansL, ansR = self.idEle, self.idEle
        while L < R:
            if L & 1:
                ansL = self.funcBinaryOperation(ansL, self.data[L])
                L += 1
            if R & 1:
                R -= 1
                ansR = self.funcBinaryOperation(self.data[R], ansR)
            L >>= 1
            R >>= 1
        return self.funcBinaryOperation(ansL, ansR)
    def BinarySearchFr(self, iFr, key):
        def onLeftSide(value):
            return True
        if iFr == self.numEle:
            return (self.numEle-1, self.numEle)
        iST = iFr + self.numPow2
        valNow = self.idEle
        while True:
            while iST%2 == 0:
                iST >>= 1
            val2 = self.funcBinaryOperation(valNow, self.data[iST])
            if not onLeftSide(val2):
                while iST < self.numPow2:
                    iST <<= 1
                    val2 = self.funcBinaryOperation(valNow, self.data[iST])
                    if onLeftSide(val2):
                        valNow = val2
                        iST += 1
                return (iST-1-self.numPow2, iST-self.numPow2)
            valNow = val2
            iST += 1
            if (iST & -iST) == iST:
                break
        return (self.numEle-1, self.numEle)
    def BinarySearchTo(self, iTo, key):
        def onRightSide(value):
            return True
        if iTo == 0:
            return (-1, 0)
        iST = iTo + self.numPow2
        valNow = self.idEle
        while True:
            iST -= 1
            while iST > 1 and iST%2:
                iST >>= 1
            val2 = self.funcBinaryOperation(self.data[iST], valNow)
            if not onRightSide(val2):
                while iST < self.numPow2:
                    iST = 2*iST+1
                    val2 = self.funcBinaryOperation(self.data[iST], valNow)
                    if onRightSide(val2):
                        valNow = val2
                        iST -= 1
                return (iST-self.numPow2, iST+1-self.numPow2)
            valNow = val2
            if (iST & -iST) == iST:
                break
        return (-1, 0)

    def printSegmentTree(self):
        As = [self.getRange(iA, iA+1) for iA in range(self.numPow2)]
        print(As)

INF = 10**18

def funcBinOpe(x, y):
    return x ^ y
idEle = 0

from random import randrange, choice, seed
import time

seed()

N, Q = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(Q)]

SegTree = SegmentTree(N, funcBinOpe, idEle)

Hs = []
setH = set()
while len(setH) < Q:
    h = randrange(1<<63)
    if h not in setH:
        Hs.append(h)
        setH.add(h)

anss = []
for noQ in range(Q):
    A, B = ABs[noQ]
    A, B = A-1, B-1
    if A > B:
        A, B = B, A

    v = SegTree.getRange(A, B+1)

    if v != 0:
        anss.append('No')
    else:
        anss.append('Yes')
        h = Hs[noQ]
        SegTree.update1(A, h)
        SegTree.update1(B, h)

print('\n'.join(anss))