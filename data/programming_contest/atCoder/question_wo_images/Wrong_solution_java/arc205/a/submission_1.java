import java.util.Scanner;
public class Main {
   public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        int Q=sc.nextInt();
        char[][] S=new char[N][N];
        int[][] A=new int[N][N];

        for(int i=0;i<N;i++){
            String s=sc.next();
            for(int j=0;j<N;j++){
                S[i][j]=s.charAt(j);
            }
        }

        for(int i=0;i<N-1;i++){
            for(int j=0;j<N-1;j++){
                if(S[i][j]=='.'&&S[i+1][j]=='.'&&S[i][j+1]=='.'&&S[i+1][j+1]=='.'){
                    A[i+1][j+1]++;
                }
            }
        }

        for(int i=1;i<N;i++){
            for(int j=1;j<N;j++){
                A[i][j]+=A[i-1][j]+A[i][j-1]-A[i-1][j-1];
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                System.out.print(A[i][j]);
            }
            System.out.println();
        }

        for(int i=0;i<Q;i++){
            int U=sc.nextInt();
            int D=sc.nextInt();
            int L=sc.nextInt();
            int R=sc.nextInt();
            int ans=0;
            U--;D--;L--;R--;
            System.out.println(A[D][R]-A[D][L]-A[U][R]+A[U][L]);
        }
        sc.close();
        return;
   }
}