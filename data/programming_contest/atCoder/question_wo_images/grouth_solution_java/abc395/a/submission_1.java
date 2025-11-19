import java.util.*;
public class Main {
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] A = new int[N];
    for (int i = 0; i < N; i++){
     A[i] = sc.nextInt();
    }
    sc.close();
    boolean isC = true;
    for (int i = 0; i < N-1; i++){
        if (A[i] >= A[i+1]){
            isC = false;
        }
    }
    System.out.println(isC? "Yes":"No");
        }}