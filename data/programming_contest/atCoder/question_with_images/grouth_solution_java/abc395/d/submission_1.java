import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int Q = sc.nextInt();

        int[] cageToLabel = new int[N + 1];
        int[] labelToCage = new int[N + 1];
        int[] pigeonToCage = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            cageToLabel[i] = i;
            labelToCage[i] = i;
            pigeonToCage[i] = i;
        }

        for (int i = 0; i < Q; i++) {
            int op = sc.nextInt();

            if (op == 1) {
                int a = sc.nextInt();
                int b = sc.nextInt();

                pigeonToCage[a] = labelToCage[b];
            } else if (op == 2) {
                int a = sc.nextInt();
                int b = sc.nextInt();

                int tmp = labelToCage[a];
                labelToCage[a] = labelToCage[b];
                labelToCage[b] = tmp;

                tmp = cageToLabel[labelToCage[a]];
                cageToLabel[labelToCage[a]] = cageToLabel[labelToCage[b]];
                cageToLabel[labelToCage[b]] = tmp;
            } else {
                int a = sc.nextInt();

                System.out.println(cageToLabel[pigeonToCage[a]]);
            }
        }
    }
}