import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        sc.nextLine();
        char [][]graph = new char[h][w];

        for(int i = 0; i < h; i++){
            String tmp = sc.nextLine();
            for(int j = 0; j < w; j++){
                graph[i][j] = tmp.charAt(j);
            }
        }

        boolean judge = true;
        int firstblad = -1;
        int finish = -1;
        int minRow = h, maxRow = -1;
        HashSet<Integer> re = new HashSet<>();

        for(int i = 0; i < h; i++){
            int rowMin = w, rowMax = -1;
            for(int j = 0; j < w; j++){
                if(graph[i][j] == '#'){
                    rowMin = Math.min(rowMin, j);
                    rowMax = Math.max(rowMax, j);
                }
            }
            if(rowMax != -1){
                re.add(i);
                minRow = Math.min(minRow, i);
                maxRow = Math.max(maxRow, i);
                if(firstblad == -1) firstblad = rowMin;
                else firstblad = Math.min(firstblad, rowMin);
                if(finish == -1) finish = rowMax;
                else finish = Math.max(finish, rowMax);
            }
        }

        for(int i = 0; i < w && judge; i++){
            boolean check = false;
            for(int j = 0; j < h; j++){
                if(graph[j][i] == '#' && !check){
                    check = true;
                }else if(graph[j][i] == '#'){
                    int t = j;
                    while(t > 0){
                        t--;
                        if(graph[t][i] == '#') break;
                        if(graph[t][i] == '.') {
                            judge = false;
                            break;
                        }
                    }
                    if(!judge) break;
                }
            }
        }

        if(judge && firstblad != -1){
            for(int i = minRow; i <= maxRow; i++){
                for(int j = firstblad; j <= finish; j++){
                    if(graph[i][j] == '.'){
                        judge = false;
                        break;
                    }
                }
                if(!judge) break;
            }
        }

        if(judge){
            for(int i = 0; i < h; i++){
                for(int j = 0; j < w; j++){
                    if(i < minRow || i > maxRow || j < firstblad || j > finish){
                        if(graph[i][j] == '#'){
                            judge = false;
                            break;
                        }
                    }
                }
                if(!judge) break;
            }
        }

        System.out.println(judge ? "Yes" : "No");
    }
}