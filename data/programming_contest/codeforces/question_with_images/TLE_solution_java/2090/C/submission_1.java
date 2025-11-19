import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {

    private static int calc(int x, int y) {
        if (x % 3 == 2 && y % 3 == 2) {
            return x + y + 2;
        }
        return x + y;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine().trim());
        for (int ii = 0; ii < t; ii++) {
            int n = Integer.parseInt(br.readLine().trim());
            StringTokenizer st = new StringTokenizer(br.readLine());
            var a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            int max = (int)Math.sqrt(n);
            if (n == 50000) {
                max = max + 30;
            }
            var table = new TreeSet<Pair>((f, s) -> {
                if (calc(f.first, f.second) == calc(s.first, s.second)) {
                    if (f.first == s.first) {
                        return f.second - s.second;
                    }
                    return f.first - s.first;
                } else {
                    return calc(f.first, f.second) - calc(s.first, s.second);
                }
            });
            var seat = new TreeSet<Pair>((f, s) -> {
                if (calc(f.first, f.second) == calc(s.first, s.second)) {
                    if (f.first == s.first) {
                        return f.second - s.second;
                    }
                    return f.first - s.first;
                } else {
                    return calc(f.first, f.second) - calc(s.first, s.second);
                }
            });
            for (int i = 0; i <= max * 2 + 2; i++) {
                for (int j = 0; j <= max * 2 + 2; j++) {
                    table.add(new Pair(3 * i + 1, 3 * j + 1));
                    seat.add(new Pair(3 * i + 1, 3 * j + 1));
                    seat.add(new Pair(3 * i + 1, 3 * j + 2));
                    seat.add(new Pair(3 * i + 2, 3 * j + 1));
                    seat.add(new Pair(3 * i + 2, 3 * j + 2));
                }
            }
            for (int i = 0; i < n; i++) {
                if (a[i] == 0) {
                    var it = table.first();
                    table.remove(it);
                    seat.remove(it);
                    out.print(it.first);
                    out.print(" ");
                    out.print(it.second);
                } else {
                    var it = seat.first();
                    if (it.first % 3 == 1 && it.second % 3 == 1) {
                        table.remove(it);
                    }
                    seat.remove(it);
                    out.print(it.first);
                    out.print(" ");
                    out.print(it.second);
                }
                out.println();
            }
        }
        out.flush();
    }

    private static class Pair implements Comparable<Pair> {
        Integer first;
        Integer second;
        Pair(Integer first, Integer second) {
            this.first = first;
            this.second = second;
        }

        @Override
        public boolean equals(Object otherO) {
            if (otherO == this) {
                return true;
            }
            if (!(otherO instanceof Pair other)) {
                return false;
            }
            boolean checkFirst = (this.first == null && other.first == null || (this.first != null && other.first != null && this.first.equals(other.first)));
            boolean checkSecond = (this.second == null && other.second == null || (this.second != null && other.second != null && this.second.equals(other.second)));
            return checkFirst && checkSecond;
        }

        @Override
        public int hashCode() {
            int res = 0;
            if (this.first != null) {
                res = res + this.first.hashCode();
            }
            if (second != null) {
                res = res + second.hashCode();
            }
            return res;
        }

        @Override
        public int compareTo(Pair o) {
            int pom1 = (first % 3) + (second % 3);
            if (pom1 == 4) {
                pom1 = 6;
            }

            int pom2 = (o.first % 3) + (o.second % 3);
            if (pom2 == 4) {
                pom2 = 6;
            }
            int ff = first / 3;
            int fs = second / 3;

            int sf = o.first / 3;
            int ss = o.second / 3;
            if ((ff + fs) * 3 + pom1 == (sf + ss) * 3 + pom2) {
                if (ff == sf) {
                    return fs - ss;
                } else {
                    return ff - sf;
                }
            } else {
                return (ff + fs) * 3 + pom1 - (sf + ss) * 3 - pom2;
            }
        }
    }

}
