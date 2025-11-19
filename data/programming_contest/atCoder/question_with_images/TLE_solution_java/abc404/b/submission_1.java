import java.util.*;
public class Main {
    static boolean f=false;
    static boolean[][] vis;
    static int n;
    static char[][] s;
    static char[][] t;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        sc.nextLine();
        s=new char[n][n];
        t=new char[n][n];
        vis=new boolean[n][n];
        for(int i=0;i<n;i++){
            String q=sc.nextLine();
            for(int j=0;j<n;j++){
                s[i][j]=q.charAt(j);
            }
        }
        for(int i=0;i<n;i++){
            String q=sc.nextLine();
            for(int j=0;j<n;j++){
                t[i][j]=q.charAt(j);
            }
        }
        int l=-1,r=101;
        while(l+1!=r){
            int m=(l+r)/2;
            f=false;
            if(check(m)){
                r=m;
            }else{
                l=m;
            }
        }
        System.out.println(r);
        sc.close();
    }
    public static boolean check(int x){
        dfs(x,0);
        if(f){
            return true;
        }
        return false;
    }
    public static void dfs(int x,int t){
        if(x==t){
            if(check2()){
                f=true;
            }
            return;
        }
        if(f){
            return;
        }
        for(int i=t+1;i<=x;i++){
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(vis[j][k]){
                        continue;
                    }
                    vis[j][k]=true;
                    if(s[j][k]=='#'){
                        s[j][k]='.';
                    }else{
                        s[j][k]='#';
                    }
                    dfs(x,i);
                    vis[j][k]=false;;
                    if(s[j][k]=='#'){
                        s[j][k]='.';
                    }else{
                        s[j][k]='#';
                    }
                }
            }
            s=rotateClockwise1(s);
            vis=rotateClockwise2(vis);
            dfs(x,t+1);
            s=rotateCounterClockwise1(s);
            vis=rotateCounterClockwise2(vis);
        }
    }
public static char[][] rotateClockwise1(char[][] matrix) {
        int n = matrix.length;
        char[][] rotated = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
    }
    public static boolean[][] rotateClockwise2(boolean[][] matrix) {
        int n = matrix.length;
        boolean[][] rotated = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        return rotated;
    }
    public static char[][] rotateCounterClockwise1(char[][] matrix) {
        int n = matrix.length;
        char[][] rotated = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[n - 1 - j][i] = matrix[i][j];
            }
        }
        return rotated;
    }
    public static boolean[][] rotateCounterClockwise2(boolean[][] matrix) {
        int n = matrix.length;
        boolean[][] rotated = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[n - 1 - j][i] = matrix[i][j];
            }
        }
        return rotated;
    }
    public static boolean check2(){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(s[i][j]!=t[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
}