import java.util.*;
public class Main
{
public static void main(String Args[])
{
Scanner sc=new Scanner(System.in);
int t=sc.nextInt();
while(t-->0)
{
int n=sc.nextInt();
int k=sc.nextInt();
int []a=new int[n];
for(int i=0;i<n;i++)
{
a[i]=sc.nextInt();
}
int pos = a[k-1];
Arrays.sort(a);
int x=-1;
for(int i=0;i<n;i++)
{
if(a[i]==pos)
{
x=i;
break;
}
}
int time=0;
String ans="YES";
for(int i=x+1;i<n;i++)
{
	int r=Math.abs(a[i]-a[i-1]);
	time+=r;
	if(time>a[i-1])
{
ans="NO";
break;
}

}
System.out.println(ans);
}
}
}
