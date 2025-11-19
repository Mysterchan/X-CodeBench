import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Main {
  public static void main(String[]args)throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    HashSet<String> pointList = new HashSet<>();
    String[] firstLine = br.readLine().split(" ");
    int N = Integer.parseInt(firstLine[0]);
    int R = Integer.parseInt(firstLine[1]);
    int C = Integer.parseInt(firstLine[2]);
    String S = br.readLine();

    int X = 0;
    int Y = 0;
    pointList.add(""+Y+X);
    for (Character c : S.toCharArray()){
      switch(c){
        case 'N':{
          R +=1;
          Y +=1;
          break;
        }
        case 'W':{
          C +=1;
          X +=1;
          break;
        }
        case 'S':{
          R -=1;
          Y -=1;
          break;
        }
        case 'E':{
          C -=1;
          X -=1;
          break;
        }
      }

      pointList.add(""+Y+ " " +X);

      if (pointList.contains(""+R+ " " +C)){
        System.out.print(1);
      }else{
        System.out.print(0);
      }
    }

  }
}