import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static PrintWriter output = new PrintWriter(System.out);
	public static void main(String[] args) {
        int H = sc.nextInt(),W = sc.nextInt();
		char[][] map = new char[H][W];
        int[] S = new int[2],G = new int[2];
        for(int i=0;i<H;i++){
            String s = sc.next();
            for(int j=0;j<W;j++){
                map[i][j] = s.charAt(j);
                if(map[i][j] == 'S'){
                    S[0] = i;
                    S[1] = j;
                }
                else if(map[i][j] == 'G'){
                    G[0] = i;
                    G[1] = j;
                }
            }
        }

        int[][][] count = new int[H][W][2];
        count[S[0]][S[1]][0] = 1;
        count[S[0]][S[1]][1] = 1;

        Set< DD387 > set = new HashSet<>();
        set.add(new DD387(S[0],S[1],0));
        set.add(new DD387(S[0],S[1],1));
        while(!set.isEmpty()){
            Set< DD387 > next = new HashSet<>();
            for(DD387 dd : set){
                int x = dd.x;
                int y = dd.y;
                int d = dd.d;

                if(d == 0){
                    if(x+1 < H && map[x+1][y] != '#'){
                        if(count[x+1][y][1] == 0){
                            count[x+1][y][1] = count[x][y][d]+1;
                            next.add(new DD387(x+1,y,1));
                        }
                        else if(count[x+1][y][1] > count[x][y][d]+1){
                            count[x+1][y][1] = count[x][y][d]+1;
                            next.add(new DD387(x+1,y,1));
                        }
                    }
                    if(0 <= x-1 && map[x-1][y] != '#'){
                        if(count[x-1][y][1] == 0){
                            count[x-1][y][1] = count[x][y][d]+1;
                            next.add(new DD387(x-1,y,1));
                        }
                        else if(count[x-1][y][1] > count[x][y][d]+1){
                            count[x-1][y][1] = count[x][y][d]+1;
                            next.add(new DD387(x-1,y,1));
                        }
                    }
                }
                else{
                    if(y+1 < W && map[x][y+1] != '#'){
                        if(count[x][y+1][0] == 0){
                            count[x][y+1][0] = count[x][y][d]+1;
                            next.add(new DD387(x,y+1,0));
                        }
                        else if(count[x][y+1][0] > count[x][y][d]+1){
                            count[x][y+1][0] = count[x][y][d]+1;
                            next.add(new DD387(x,y+1,0));
                        }
                    }
                    if(0 <= y-1 && map[x][y-1] != '#'){
                        if(count[x][y-1][0] == 0){
                            count[x][y-1][0] = count[x][y][d]+1;
                            next.add(new DD387(x,y-1,0));
                        }
                        else if(count[x][y-1][0] > count[x][y][d]+1){
                            count[x][y-1][0] = count[x][y][d]+1;
                            next.add(new DD387(x,y-1,0));
                        }
                    }
                }
            }
            set = next;
            if(count[G[0]][G[1]][0] != 0 || count[G[0]][G[1]][1] != 0) break;
        }

        int ans = Math.min(count[G[0]][G[1]][0]==0 ? Integer.MAX_VALUE : count[G[0]][G[1]][0],
                count[G[0]][G[1]][1]==0 ? Integer.MAX_VALUE : count[G[0]][G[1]][1]);

        output.println(ans-1);

		output.flush();
		sc.close();
	}
}

class DD387{
	int x,y,d;
    DD387(int x,int y,int d){
        this.x = x;
        this.y = y;
        this.d = d;
    }

}