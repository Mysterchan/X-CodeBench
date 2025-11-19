import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int a[] = Arrays.stream(new int[n]).map(e -> sc.nextInt()).toArray();

        boolean used[] = new boolean[n];
        int result = 0;
        int from = 1;
        int to = n - 1;

        for(int i = n - 1; i >= 0; i--) {
            if(used[i]) {
                continue;
            }

            int index = upperBound(a, a[i] / 2, to);

            if(index < 0) {

                index++;
                index *= -1;
                index--;

                if(index < 0) {
                    break;
                }
            }

            result++;
            from = index + 1;
            to = index;
            used[index] = true;

        }

        System.out.println(result);

    }

    static int lowerBound (int[] a, int key, int from) {
        int index = Arrays.binarySearch(a, from, a.length, key);

        if(index < 0) {
            return index;
        }

        for(int i = index; i > 0; i--) {
            if(a[i] != a[i - 1]) {
                index = i;
                break;
            }
        }

        return index;
    }

    static int upperBound (int[] a, int key, int to) {
        int index = Arrays.binarySearch(a, 0, to, key);

        if(index < 0) {
            return index;
        }

        for(int i = index + 1; i < to ; i++) {
            if(a[i] == a[i - 1]) {
                index = i;
            }
            else {
                break;
            }
        }

        return index;
    }
}