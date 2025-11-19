import java.io.*;public class Main{
static int[][]b={{1,4},{3,2}};
static long f(int x,int y,int s,long a){
if(s==2)return a+b[x][y]-1;
int h=s/2;long q=(long)h*h;
if(x<h&&y<h)return f(x,y,h,a);
if(x>=h&&y>=h)return f(x-h,y-h,h,a+q);
if(x>=h)return f(x-h,y,h,a+2*q);
return f(x,y-h,h,a+3*q);
}
static int[]g(long d,int s,long a,int u,int v){
if(s==2){
for(int i=0;i<2;i++)for(int j=0;j<2;j++)
if(a+b[i][j]-1==d)return new int[]{u+i+1,v+j+1};
}
int h=s/2;long q=(long)h*h;
if(d<a+q)return g(d,h,a,u,v);
if(d<a+2*q)return g(d,h,a+q,u+h,v+h);
if(d<a+3*q)return g(d,h,a+2*q,u+h,v);
return g(d,h,a+3*q,u,v+h);
}
public static void main(String[]a)throws IOException{
BufferedReader r=new BufferedReader(new InputStreamReader(System.in));
PrintWriter w=new PrintWriter(System.out);
int t=Integer.parseInt(r.readLine());
while(t-->0){
int n=Integer.parseInt(r.readLine()),q=Integer.parseInt(r.readLine()),s=1<<n;
while(q-->0){
String[]p=r.readLine().split(" ");
if(p[0].equals("->")){
int x=Integer.parseInt(p[1])-1,y=Integer.parseInt(p[2])-1;
w.println(f(x,y,s,1));
}else{
long d=Long.parseLong(p[1]);
int[]z=g(d,s,1,0,0);
w.println(z[0]+" "+z[1]);
}
}
}
w.flush();
}}
