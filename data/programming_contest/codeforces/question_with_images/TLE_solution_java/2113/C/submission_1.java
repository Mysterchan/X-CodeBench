import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
    public static void main(String[] args) throws java.lang.Exception
    {
       Scanner sc = new Scanner(System.in);
        int tt = sc.nextInt();
        for (int ww = 0; ww < tt; ww++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
           char arr[][]=new char[n][m];
            for (int j = 0; j < n; j++) {
                arr[j]=sc.next().toCharArray();
           }
           int gold=0;
           boolean isSpace=false;
           int blow=Integer.MAX_VALUE;
           for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){

                if(arr[i][j]=='g'){
                    gold++;
                }
                if(arr[i][j]!='.'){
                    continue;
                }
                isSpace=true;
                int temp=0;
                if(k==1){
                    blow=0;
                }else{
                    int row1=Math.max(0,i-k+1);
                    int row2=Math.min(n-1,i+k-1);
                    int col1=Math.max(0,j-k+1);
                    int col2=Math.min(m-1,j+k-1);
                    for(int ii=row1;ii<=row2;ii++){
                        for(int jj=col1;jj<=col2;jj++){
                            if(arr[ii][jj]=='g'){
                                temp++;
                            }
                        }
                    }
                    blow=Math.min(blow,temp);
                }


            }
           }
           if(!isSpace){
            System.out.println(0);
           }else{
            System.out.println(gold-blow);
           }


        }
    }
}
