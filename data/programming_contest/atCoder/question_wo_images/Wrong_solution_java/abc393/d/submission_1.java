import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        int size = 0;
        for(int i=0;i<n;i++){
            if(s.charAt(i) == '1'){
                size++;
            }
        }

        int arr[] = new int[size];
        int j=0;
        for(int i=0;i<n;i++){
            if(s.charAt(i) == '1'){
                arr[j] = i;
                j++;
            }
        }

        int mid = size/2;
        int idx = arr[mid];
        int step = 0;
        if(size>1){
            for(int i=0;i<size;i++){
                int inside = Math.abs((arr[i]-i) -(idx-mid));
                step += inside;
            }
            System.out.println(step);
        }
        else{
            System.out.println(0);
        }
	}
}