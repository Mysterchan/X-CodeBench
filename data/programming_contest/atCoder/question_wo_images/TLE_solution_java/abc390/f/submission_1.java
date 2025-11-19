import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int map[] = new int[N];
		for(int i = 0;i < N;i++) {
			map[i] = sc.nextInt()-1;
		}
		int ans = 0;
		for(int i = 0;i < N;i++) {
			int result[] = new int[N];
			int min = map[i];
			int max = map[i];
			result[min] = 1;
			int sum = 1;
			for(int n = i;n < N;n++) {

				if(min > map[n]) {
					min = map[n];
					result[min] = 1;
					if(result[min+1] == 0) {
						sum += 1;
					}
				}else if(max < map[n]) {
					max = map[n];
					result[max] = 1;
					if(result[max-1] == 0) {
						sum += 1;
					}
				}else if(result[map[n]] == 0){
					result[map[n]] = 1;
					if(map[n] != max && map[n] != min && result[map[n]+1] == 1 && result[map[n]-1] == 1) {
						sum -= 1;
					}else if(map[n] != max && map[n] != min && result[map[n]+1] == 0 && result[map[n]-1] == 0){
						sum+=1;
					}
				}

				ans += sum;
			}
		}
		System.out.println(ans);

	}

}