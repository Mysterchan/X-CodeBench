import java.util.*;
public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int N = sc.nextInt();
       int[] A = new int[N];
       int[] B = new int[N];
       for(int i= 0; i < N; i++){
        A[i] = sc.nextInt();
       }
       for(int i= 0; i < N; i++){
        B[i] = sc.nextInt();
       }
       for(int i= 0; i < N; i++){
        for(int j = 0; j <N; j++){
         if(B[j] == i+1){
          System.out.print(B[A[j]-1]);
          System.out.print(" ");
         }
        }
      }
    }}