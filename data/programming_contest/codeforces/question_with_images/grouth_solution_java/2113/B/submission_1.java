import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
		   long w=sc.nextLong(),h=sc.nextLong(),a=sc.nextLong(),b=sc.nextLong();
		   long x1=sc.nextLong(),y1=sc.nextLong(),x2=sc.nextLong(),y2=sc.nextLong();
		   if((Math.abs(x1-x2)%a==0&&x1!=x2)||(Math.abs(y1-y2)%b==0&&y1!=y2)||(x1==x2&&y1==y2)) System.out.println("Yes");
		   else System.out.println("No");

		}

	}
}
