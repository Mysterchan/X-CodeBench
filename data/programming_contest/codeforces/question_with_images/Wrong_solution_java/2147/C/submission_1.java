import java.util.Scanner;
import java.util.*;
import java.io.*;
import java.math.*;
import static java.lang.Math.min;
import static java.lang.Math.max;
import static java.lang.Math.abs;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int ti = sc.nextInt();
        while (ti-- > 0) {
            int n = sc.nextInt();
            String str = sc.next();
            StringBuilder sb = new StringBuilder();
            for (int i = n-1; i >= 0; i--) {
                sb.append(str.charAt(i));
            }

            String rev = sb.toString();
            Boolean front = helper(str);
            Boolean back = helper(rev);

            System.out.println((front || back) ? "YES" : "NO");
        }
        sc.close();
    }

    public static boolean helper(String str){
        int n = str.length();

        for (int i = 0; i < n; i++) {
            if(str.charAt(i) == '1') continue;

            if(i == n-1) continue;

            if(str.charAt(i+1) == '0') i++;
            else if(i < n-2 && str.charAt(i+2) == '0') i+=2;
            else return false;
        }

        return true;
    }

public static int bs(long[] arr, long target) {
        int start = 0, end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) start = mid + 1;
            else end = mid - 1;
        }
        return end;
    }

static long sumOfDigits(long n) {
    long result = 0;
    long factor = 1;
    while (n / factor > 0) {
        long lower = n - (n / factor) * factor;
        long curr = (n / factor) % 10;
        long higher = n / (factor * 10);

        result += higher * (factor * 45);
        result += (curr * (curr - 1) / 2) * factor;
        result += curr * (lower + 1);

        factor *= 10;
    }
    return result;
}
public static long modPow(long base, long exp, long mod) {
        long result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
public static long add(long a, long b, long mod) { return ((a%mod) + (b%mod)) % mod; }
public static long sub(long a, long b, long mod) { return ((a%mod) - (b%mod)) % mod; }
public static long mul(long a, long b, long mod) { return ((a%mod) * (b%mod)) % mod; }
public static long inv(long a, long mod) { return modPow(a, mod - 2, mod); }

static <K> void inc(Map<K, Long> map, K key) {
    map.put(key, map.getOrDefault(key, 0L) + 1);
}
static void sort(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            list.add(arr[i]);
        }
        Collections.sort(list);
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return;
    }

static void sort(long[] arr) {
        ArrayList<Long> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            list.add(arr[i]);
        }
        Collections.sort(list);
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return;
    }

static boolean allsame(int[] arr) {
        for (int i : arr) {
            if (arr[0] != i) return false;
        }
        return true;
    }

static boolean allsame(long[] arr) {
        for (long i : arr) {
            if (arr[0] != i) return false;
        }
        return true;
    }

static int lcm(int x, int y) { return (x * y) / gcd(x, y); }

static long lcm(long x, long y) { return (x * y) / gcd(x, y); }

static int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }

static long gcd(long x, long y) {
        while (y != 0) {
            long temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
static long maxSubarraySum(long[] arr) {
        long maxSoFar = arr[0], currMax = arr[0];
        for (int i = 1; i < arr.length; i++) {
            currMax = Math.max(arr[i], currMax + arr[i]);
            maxSoFar = Math.max(maxSoFar, currMax);
        }
        return maxSoFar;
    }
}
