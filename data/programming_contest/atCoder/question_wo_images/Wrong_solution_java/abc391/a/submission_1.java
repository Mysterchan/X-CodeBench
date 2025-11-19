import java.util.*;

public class Main{
    public static void main(String [] args){
        Scanner sc =new Scanner(System.in);
        String input =sc.nextLine();
        StringBuilder str = new StringBuilder();

        for(int i=0;i<input.length();i++){
            if(input.charAt(i)=='N'){
                str.append('S');
            }
            else if(input.charAt(i)=='S'){
                str.append('N');

            }
            else if(input.charAt(i)=='W'){
                str.append('W');

            }
            else if(input.charAt(i)=='E'){
                str.append('W');

            }
        }
        System.out.print(str.toString());
    }
}