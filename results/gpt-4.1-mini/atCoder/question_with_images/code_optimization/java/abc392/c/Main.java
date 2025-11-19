import java.util.*;
public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int N = sc.nextInt();
       int[] P = new int[N];
       int[] Q = new int[N];
       for(int i= 0; i < N; i++){
           P[i] = sc.nextInt();
       }
       for(int i= 0; i < N; i++){
           Q[i] = sc.nextInt();
       }
       
       // Create an array to map bib number to person index
       int[] bibToPerson = new int[N+1];
       for(int i = 0; i < N; i++){
           bibToPerson[Q[i]] = i;
       }
       
       StringBuilder sb = new StringBuilder();
       for(int i = 1; i <= N; i++){
           int personIndex = bibToPerson[i];
           int staringAtPerson = P[personIndex];
           int staringAtBib = Q[staringAtPerson - 1];
           sb.append(staringAtBib).append(" ");
       }
       System.out.println(sb.toString().trim());
    }
}