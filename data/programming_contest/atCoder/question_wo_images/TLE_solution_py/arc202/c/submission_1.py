import math
import sys
sys.set_int_max_str_digits(300000)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

a = input()
nums = list(map(int, input().split()))
for i in range(len(nums)):
    nums[i] = int("1"*nums[i])
ans=nums[0]
print(ans%998244353)
for i in range(1,len(nums)):
    ans=lcm(ans,nums[i])
    print(lcm(ans,nums[i])%998244353)