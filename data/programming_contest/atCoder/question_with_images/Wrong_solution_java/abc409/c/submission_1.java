import java.util.ArrayList;
import java.util.Scanner;

class Main{
   public static void main(String[]args){
	 Scanner sc = new Scanner(System.in);
	 ArrayList<Integer> List = new ArrayList<Integer>();
	 ArrayList<String> SList = new ArrayList<String>();
	 int N = sc.nextInt();
	 int L = sc.nextInt();
	 int Num = 0;
	 int AllNum = 0;
	 List.add(1);
	 if(L % 3 == 0){
	 }else{System.out.println(0);System.exit(0);}
	 for(int i = 0;i < L - 1;i++){
	   List.add(0);
	 }
	 for(int i = 0;i < N - 1;i++){
	   Num += sc.nextInt();
	   for(;;){
		 if(Num >= L){
		   Num -= L;
		 }else{break;}
	   }
	   List.set(Num,List.get(Num) + 1);
	 }
	 int l = L / 3;
	 for(int i = 0;i < l;i++){
	   int a = List.get(i);
	   if(a == 0){
	   }else{
		 int b = List.get(i + l);
		 if(b == 0){
		 }else{
		   int c = List.get(i + l + l);
		   int All = a;
		   All = All * b;
		   All = All * c;
		   AllNum += All;
		 }
	   }
	 }
	 System.out.println(AllNum);
   }
}