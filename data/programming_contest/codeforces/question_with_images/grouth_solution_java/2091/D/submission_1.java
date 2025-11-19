import java.util.Scanner;
public class Main{
    public static void main(String[] mulish)
    {
        Scanner sc=new Scanner(System.in);
        int t= sc.nextInt();
        while(t-->0) {
            int n= sc.nextInt(), m=sc.nextInt(),k=sc.nextInt();
            int z=(k+n-1)/n;
            System.out.println((m/(m-z+1)));

        }
    }
}
