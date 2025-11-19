import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       int n=sc.nextInt();
       int mat[][]=new int[n][n];

        for(int i=0;i<n;i++){
            int row=i;
            int col=n-1-i;
            if(row>col) continue;

            boolean vis[][]=new boolean[n][n];
            Queue<pair>q=new LinkedList<>();
            q.add(new pair(i,i));
            int delrow[]={-1,0,1,0};
            int delcol[]={0,1,0,-1};
            while(!q.isEmpty()){

                pair p=q.remove();
                int r=p.r;
                int c=p.c;
                vis[r][c]=true;
                for(int k=0;k<4;k++){
                    int nrow=r+delrow[k];
                    int ncol=c+delcol[k];
                    if(nrow>=0&&nrow<n&&ncol>=0&&ncol<n&&vis[nrow][ncol]==false){
                        if(nrow>=row&&nrow<=col&&ncol>=row&&ncol<=col){
                            q.add(new pair(nrow,ncol));
                        }
                    }
                }
            }

            int res=0;
            if(row%2!=0){
                res=1;
            }

            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(vis[j][k]==true){
                        mat[j][k]=res;
                    }
                }
            }

        }

        char res[][]=new char[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mat[i][j]==0){
                    res[i][j]='#';
                }
                else{
                    res[i][j]='.';
                }
            }
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print(res[i][j]);
            }
            System.out.println();
        }

    }
    static class pair{
        int r;
        int c;
        pair(int r,int c){
            this.r=r;;
            this.c=c;
        }
    }

}