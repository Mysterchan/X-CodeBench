from collections import defaultdict
import math
from math import gcd
class Vector:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y

    def __add__(self,other:"Vector")->"Vector":
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other:"Vector")->"Vector":
        return Vector(self.x-other.x,self.y-other.y)

    def __repr__(self):
        return f"{self.x} {self.y}"

    def __mul__(self,k:float)->"Vector":
        return Vector(self.x*k , self.y*k)

    def __truediv__(self, k: float) -> "Vector":
        return Vector(self.x / k, self.y / k)

    def dot(self,other:"Vector"):
        return self.x*other.x + self.y*other.y

    def norm(self):
        return (self.dot(self))**(1/2)

    def angle(self) -> float:
        return math.atan2(self.y, self.x)

    def normalize(self) -> "Vector":
        n = self.norm()
        if n == 0:
            raise ValueError("Zero vector cannot be normalized")
        return self / n

    def nnormalize(self)->"Vector":
        g=gcd(self.x,self.y)
        return self/g

def solve(n,vl ):
    D = defaultdict(int)
    E = defaultdict(int)

    for i in range(n):
      v0=vl[i]
      for j in range(i+1, n):
        v=vl[j]-v0
        if v.y < 0 or (v.y == 0 and v.x < 0):
            v=v*(-1)
        E[(v.x,v.y)] += 1
        v=v.nnormalize()
        D[(v.x,v.y)] += 1
    print(D)
    p = sum(num * (num-1) // 2 for num in D.values())
    q = sum(num * (num-1) // 2 for num in E.values())
    return p - q//2

if __name__ == "__main__":
    n = int(input())
    vl=[]
    for i in range(n):
        x,y=map(int,input().split())
        vl.append(Vector(x,y))
    print(solve(n, vl))