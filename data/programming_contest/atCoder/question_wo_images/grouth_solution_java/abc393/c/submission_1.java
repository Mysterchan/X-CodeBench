import java.util.*;
import java.util.stream.*;
import java.math.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int ans = 0;
        HashSet<Pair> graph = new HashSet<>();
        for(int i = 1; i <= n; i++){
            Pair tmp = new Pair(i,i);
            graph.add(tmp);
        }
        for (int i = 0; i < m; i++){
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            Pair num = new Pair(v1,v2);
            Pair num2 = new Pair(v2,v1);
            if(graph.contains(num) || graph.contains(num2)) ans ++;
            else graph.add(num);
        }
        System.out.println(ans);
    }

static class Pair {
    int value;
    int count;

    Pair(int value, int count) {
        this.value = value;
        this.count = count;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Pair)) return false;
        Pair p = (Pair) o;
        return count == p.count && value == p.value;
    }

    @Override
    public int hashCode() {
        return Objects.hash(count, value);
    }
}

}