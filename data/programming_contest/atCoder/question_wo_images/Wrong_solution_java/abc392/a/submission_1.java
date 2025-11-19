import java.util.Scanner;

public class Main {

    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        int[] A = new int[3];

        for(int i = 0;i<3;i++){
            A[i] = scanner.nextInt();
        }
        for(int i = 0;i<A.length-1;i++){
            for(int j =i+1;j<A.length;j++){
                for(int f = 0;f<A.length;f++){

                    if(A[i]*A[j]==A[f] ){
                        if(A[f]==A[i]||A[f]==A[j]){
                            if(A[f]==1){
                                System.out.print("Yes");
                                return;
                            }else{
                                System.out.print("No");
                                return;
                            }
                        }else{
                            System.out.print("Yes");
                                return;
                        }
                    }

                }
            }
        }
        System.out.print("No");

    }
}