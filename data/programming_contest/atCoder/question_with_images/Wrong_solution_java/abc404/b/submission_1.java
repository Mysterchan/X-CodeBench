import java.util.ArrayList;
import java.util.Scanner;

class Main{
   public static void main(String[]args){
	 Scanner sc = new Scanner(System.in);
	 ArrayList<Integer> List = new ArrayList<Integer>();
	 ArrayList<String> SList = new ArrayList<String>();
	 ArrayList<String> SList2 = new ArrayList<String>();
	 int N = sc.nextInt();
	 int Min = 100000;
	 int MinNum = 0;
	 for(int i = 0;i < N;i++){
	   SList.add(sc.next());
	 }
	 for(int i = 0;i < N;i++){
	   SList2.add(sc.next());
	 }
	 N = N - 1;
	 if(N == 0){
	   if(SList.get(0).equals(SList2.get(0))){
	     System.out.println(0);
	   }else{System.out.println(1);}
	   System.exit(0);
	 }
	 for(int i = 0;i < 4;i++){
	   int Nuw = 0;
	   if(i == 1){
		 for(int y = 0;y < N + 1;y++){
		   for(int x = 0;x < N + 1;x++){
			 if(SList.get(y).substring(x,x + 1).equals(SList2.get(x).substring(N - y,(N - y) + 1))){
			 }else{Nuw++;}
		   }
		 }
	   }
	   if(i == 2){
	 	 for(int y = 0;y < N + 1;y++){
		   for(int x = 0;x < N + 1;x++){
			 if(SList.get(y).substring(x,x + 1).equals(SList2.get(N - y).substring(N - x,(N - x) + 1))){
			 }else{Nuw++;}
		   }
		 }
	   }
	   if(i == 3){
	 	 for(int y = 0;y < N + 1;y++){
		   for(int x = 0;x < N + 1;x++){
			 if(SList.get(y).substring(x,x + 1).equals(SList2.get(N - x).substring(y,y + 1))){
			 }else{Nuw++;}
		   }
		 }
	   }
	   if(i == 0){
	 	 for(int y = 0;y < N+ 1;y++){
		   for(int x = 0;x < N + 1;x++){
			 if(SList.get(y).substring(x,x + 1).equals(SList2.get(y).substring(x,x + 1))){
			 }else{Nuw++;}
		   }
		 }
	   }
	   if(Min > Nuw + i){
		 Min = Nuw;
		 MinNum = i;
	   }
	 }
	 System.out.println(Min + MinNum);
   }
}