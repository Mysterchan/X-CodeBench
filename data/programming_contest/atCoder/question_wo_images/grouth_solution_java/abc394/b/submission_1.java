import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String[] strings = new String[N];

        for (int i = 0; i < N; i++) {
            strings[i] = sc.next();
        }

        sc.close();

        Arrays.sort(strings, Comparator.comparingInt(String::length));

        StringBuilder result = new StringBuilder();
        for (String s : strings) {
            result.append(s);
        }

        System.out.println(result.toString());
    }
}