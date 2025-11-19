import java.util.*;
import java.io.*;

public class Main {
    static long mod = (int)1e9 + 7;

    public static long pow(long a, long b) {
        long re = 1;
        while (b > 0) {
            if ((b & 1) == 1) {
                re = (re * a) % mod;
            }
            a = (a * a) % mod;
            b >>= 1;
        }
        return re;
    }

    public static void revArr(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    public static void sort(int[] a) {
        mergeSort(a, 0, a.length - 1);
    }

    private static void mergeSort(int[] arr, int left, int right) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1, n2 = right - mid;
        int[] L = new int[n1], R = new int[n2];
        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int tt = 1;
        while (tt-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            ArrayList<Integer> list[] = new ArrayList[n];
            for(int  i = 0;i < n;i++){
                list[i] = new ArrayList<>();
            }
            int degree[] = new int[n];
            for(int i =0 ;i < m;i++){
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                u--;
                v--;
                list[u].add(v);

                list[v].add(u);
                degree[u]++;
                degree[v]++;
            }

            boolean found = true;
            for(int i= 0;i < n;i++){
                if(degree[i] != 2) found = false;
            }
            int count = 0;
            boolean vis[] = new boolean[n];
            for(int i = 0;i < n;i++){
                if(!vis[i]){
                    dfs(i, -1, list, vis);
                    count++;
                }
            }
            if(count > 1)found =false;
            if(found){
                pw.println("Yes");
            }
            else pw.println("No");

        }
        pw.flush();
    }
    public static void dfs(int curr,int par,ArrayList<Integer> list[],boolean vis[]){
        vis[curr]  = true;
        boolean found = false;
        for(int j : list[curr]){
            if( j == par) continue;
            if(vis[j]) return;
             dfs(j, curr, list, vis);

        }

    }
}