import java.util.*;
public class Main{
public static void main(String[]a){
Scanner s=new Scanner(System.in);
int t=s.nextInt();
while(t-->0){
int n=s.nextInt();
List<int[]> arrays=new ArrayList<>();
int maxLen=0;
for(int i=0;i<n;i++){
int k=s.nextInt();
int[] arr=new int[k];
for(int j=0;j<k;j++)arr[j]=s.nextInt();
arrays.add(arr);
if(k>maxLen)maxLen=k;
}
StringBuilder sb=new StringBuilder();
int cur=0;
while(cur<maxLen){
int best=-1;
for(int i=0;i<n;i++){
int[] arr=arrays.get(i);
if(arr.length<=cur)continue;
if(best==-1)best=i;
else{
int[] bArr=arrays.get(best);
int lim=Math.min(arr.length,bArr.length);
int cmp=0;
for(int j=cur;j<lim;j++){
if(arr[j]!=bArr[j]){
cmp=(arr[j]<bArr[j]?-1:1);
break;
}
}
if(cmp==0)cmp=(arr.length<bArr.length?-1:(arr.length>bArr.length?1:0));
if(cmp<0)best=i;
}
}
int[] chosen=arrays.get(best);
for(int k=cur;k<chosen.length;k++)sb.append(chosen[k]).append(" ");
cur=chosen.length;
}
String res=sb.toString().trim();
System.out.println(res);
}
}
}
