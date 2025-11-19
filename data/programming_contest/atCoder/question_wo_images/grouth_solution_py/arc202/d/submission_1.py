import sys,random,bisect
from collections import deque,defaultdict
from heapq import heapify,heappop,heappush
from itertools import permutations
from math import gcd,log

input = lambda :sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

mod = 998244353
omega = pow(3,119,mod)
rev_omega = pow(omega,mod-2,mod)

N = 2*10**5
g1 = [1]*(N+1)
g2 = [1]*(N+1)
inv = [1]*(N+1)

for i in range( 2, N + 1 ):
    g1[i]=( ( g1[i-1] * i ) % mod )
    inv[i]=( ( -inv[mod % i] * (mod//i) ) % mod )
    g2[i]=( (g2[i-1] * inv[i]) % mod )
inv[0]=0

_fft_mod = 998244353
_fft_imag = 911660635
_fft_iimag = 86583718
_fft_rate2 = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601,
              842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899)
_fft_irate2 = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960,
               354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235)
_fft_rate3 = (372528824, 337190230, 454590761, 816400692, 578227951, 180142363, 83780245, 6597683, 70046822, 623238099,
              183021267, 402682409, 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204)
_fft_irate3 = (509520358, 929031873, 170256584, 839780419, 282974284, 395914482, 444904435, 72135471, 638914820, 66769500,
               771127074, 985925487, 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681)

def _butterfly(a):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = 0
    while len_ < h:
        if h - len_ == 1:
            p = 1 << (h - len_ - 1)
            rot = 1
            for s in range(1 << len_):
                offset = s << (h - len_)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * rot % _fft_mod
                    a[i + offset] = (l + r) % _fft_mod
                    a[i + offset + p] = (l - r) % _fft_mod
                if s + 1 != (1 << len_):
                    rot *= _fft_rate2[(~s & -~s).bit_length() - 1]
                    rot %= _fft_mod
            len_ += 1
        else:
            p = 1 << (h - len_ - 2)
            rot = 1
            for s in range(1 << len_):
                rot2 = rot * rot % _fft_mod
                rot3 = rot2 * rot % _fft_mod
                offset = s << (h - len_)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p] * rot
                    a2 = a[i + offset + p * 2] * rot2
                    a3 = a[i + offset + p * 3] * rot3
                    a1na3imag = (a1 - a3) % _fft_mod * _fft_imag
                    a[i + offset] = (a0 + a2 + a1 + a3) % _fft_mod
                    a[i + offset + p] = (a0 + a2 - a1 - a3) % _fft_mod
                    a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % _fft_mod
                    a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % _fft_mod
                if s + 1 != (1 << len_):
                    rot *= _fft_rate3[(~s & -~s).bit_length() - 1]
                    rot %= _fft_mod
            len_ += 2

def _butterfly_inv(a):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = h
    while len_:
        if len_ == 1:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 1)):
                offset = s << (h - len_ + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % _fft_mod
                    a[i + offset + p] = (l - r) * irot % _fft_mod
                if s + 1 != (1 << (len_ - 1)):
                    irot *= _fft_irate2[(~s & -~s).bit_length() - 1]
                    irot %= _fft_mod
            len_ -= 1
        else:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 2)):
                irot2 = irot * irot % _fft_mod
                irot3 = irot2 * irot % _fft_mod
                offset = s << (h - len_ + 2)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p]
                    a2 = a[i + offset + p * 2]
                    a3 = a[i + offset + p * 3]
                    a2na3iimag = (a2 - a3) * _fft_iimag % _fft_mod
                    a[i + offset] = (a0 + a1 + a2 + a3) % _fft_mod
                    a[i + offset + p] = (a0 - a1 +
                                         a2na3iimag) * irot % _fft_mod
                    a[i + offset + p * 2] = (a0 + a1 -
                                             a2 - a3) * irot2 % _fft_mod
                    a[i + offset + p * 3] = (a0 - a1 -
                                             a2na3iimag) * irot3 % _fft_mod
                if s + 1 != (1 << (len_ - 1)):
                    irot *= _fft_irate3[(~s & -~s).bit_length() - 1]
                    irot %= _fft_mod
            len_ -= 2

def _convolution_naive(a, b):
    n = len(a)
    m = len(b)
    ans = [0] * (n + m - 1)
    if n < m:
        for j in range(m):
            for i in range(n):
                ans[i + j] = (ans[i + j] + a[i] * b[j]) % _fft_mod
    else:
        for i in range(n):
            for j in range(m):
                ans[i + j] = (ans[i + j] + a[i] * b[j]) % _fft_mod
    return ans

def _convolution_fft(a, b):
    a = a.copy()
    b = b.copy()
    n = len(a)
    m = len(b)
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    _butterfly(a)
    b += [0] * (z - m)
    _butterfly(b)
    for i in range(z):
        a[i] = a[i] * b[i] % _fft_mod
    _butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, _fft_mod - 2, _fft_mod)
    for i in range(n + m - 1):
        a[i] = a[i] * iz % _fft_mod
    return a

def _convolution_square(a):
    a = a.copy()
    n = len(a)
    z = 1 << (2 * n - 2).bit_length()
    a += [0] * (z - n)
    _butterfly(a)
    for i in range(z):
        a[i] = a[i] * a[i] % _fft_mod
    _butterfly_inv(a)
    a = a[:2 * n - 1]
    iz = pow(z, _fft_mod - 2, _fft_mod)
    for i in range(2 * n - 1):
        a[i] = a[i] * iz % _fft_mod
    return a

def convolution(a, b):

    n = len(a)
    m = len(b)
    if n == 0 or m == 0:
        return []
    if min(n, m) <= 0:
        return _convolution_naive(a, b)
    if a is b:
        return _convolution_square(a)
    return _convolution_fft(a, b)

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    return (g1[n] * g2[r] % mod) * g2[n-r] % mod

mod = 998244353
N = 5*10**5
g1 = [1]*(N+1)
g2 = [1]*(N+1)
inverse = [1]*(N+1)

for i in range( 2, N + 1 ):
    g1[i]=( ( g1[i-1] * i ) % mod )
    inverse[i]=( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2[i]=( (g2[i-1] * inverse[i]) % mod )
inverse[0]=0

def sub_calc_slow(H,T,a,c):

    f = [0] * (2*H+2)
    f[a] = 1
    f[2*H-a] = -1
    for _ in range(T):
        nf = f[:]
        for i in range(2*H+2):
            nf[(i+1) % (2*H+2)] += f[i]
            nf[(i+1) % (2*H+2)] %= mod
            nf[i-1] += f[i]
            nf[i-1] %= mod
        f = nf
    return f[c]

def solve_slow(H,W,T,a,b,c,d):
    a,b,c,d = a-1,b-1,c-1,d-1

    res = 0
    for dont_move in range(T+1):
        if dont_move & 1 == 0:
            res += cmb(T,dont_move,mod) * sub_calc_slow(H,T-dont_move,a,c) * sub_calc_slow(W,T-dont_move,b,d)
            res %= mod
        else:
            res -= cmb(T,dont_move,mod) * sub_calc_slow(H,T-dont_move,a,c) * sub_calc_slow(W,T-dont_move,b,d)
            res %= mod
    return res

def sub_calc_1(H,T,a,c):
    res = []

    f = [0] * (2*H+2)
    f[a] = 1
    f[2*H-a] = -1
    res.append(f[c])
    for _ in range(T):
        nf = f[:]
        for i in range(2*H+2):
            nf[(i+1) % (2*H+2)] += f[i]
            nf[(i+1) % (2*H+2)] %= mod
            nf[i-1] += f[i]
            nf[i-1] %= mod
        f = nf
        res.append(f[c])
    return res

def sub_calc_2(H,T,a,c):

    f = [0] * (T+1)
    for d in range(c,T+2*H-a+1,2*H+2):
        for i in range(T+1):
            if 2*i+d-a <= T and i+d-a >= 0:
                f[2*i+d-a] += g2[i] * g2[i+d-a] % mod
                f[2*i+d-a] %= mod
            if i+d-(2*H-a) >= 0 and 2*i+d-(2*H-a) <= T:
                f[2*i+d-(2*H-a)] -= g2[i] * g2[i+d-(2*H-a)] % mod
                f[2*i+d-(2*H-a)] %= mod

    for d in range(c,-(T+2*H-a+1),-2*H-2):
        if d == c:
            continue
        for i in range(T+1):
            if 2*i+d-a <= T and i+d-a >= 0:
                f[2*i+d-a] += g2[i] * g2[i+d-a] % mod
                f[2*i+d-a] %= mod
            if i+d-(2*H-a) >= 0 and 2*i+d-(2*H-a) <= T:
                f[2*i+d-(2*H-a)] -= g2[i] * g2[i+d-(2*H-a)] % mod
                f[2*i+d-(2*H-a)] %= mod

    g = [g2[i] for i in range(T+1)]

    h = convolution(f,g)
    return [h[n]*g1[n] % mod for n in range(T+1)]

def solve_fast(H,W,T,a,b,c,d):
    a,b,c,d = a-1,b-1,c-1,d-1

    x_res,y_res = [],[]
    if 2*H*(2*H+2) <= T:
        x_res = sub_calc_1(H,T,a,c)
    else:
        x_res = sub_calc_2(H,T,a,c)

    if 2*W*(2*W+2) <= T:
        y_res = sub_calc_1(W,T,b,d)
    else:
        y_res = sub_calc_2(W,T,b,d)

    res = 0
    for dont_move in range(T+1):
        if dont_move & 1 == 0:
            res += cmb(T,dont_move,mod) * (x_res[T-dont_move] * y_res[T-dont_move] % mod) % mod
            res %= mod
        else:
            res -= cmb(T,dont_move,mod) * (x_res[T-dont_move] * y_res[T-dont_move] % mod) % mod
            res %= mod
    return res

H,W,T,a,b,c,d = mi()
print(solve_fast(H,W,T,a,b,c,d))