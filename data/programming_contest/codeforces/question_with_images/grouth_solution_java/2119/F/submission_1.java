import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;

public final class Main {

    private static int MAX_V = 500005;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(s.nextToken());
        int[][] time = new int[MAX_V][2];
        int[][] lives = new int[MAX_V][2];
        int[][] volcanoD = new int[MAX_V][2];
        int[] q = new int[2 * MAX_V];
        byte[] qT = new byte[2 * MAX_V];
        int[] prev = new int[2 * MAX_V];
        int[] volcano = new int[MAX_V];
        int[] st = new int[MAX_V];
        for (int t = 0; t < T; ++t) {
            s = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(s.nextToken());
            int start = Integer.parseInt(s.nextToken());
            s = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; ++i) {
                st[i] = Integer.parseInt(s.nextToken());
            }
            List<List<Integer>> edges = new ArrayList<>();
            for (int i = 0; i <= n; ++i) {
                edges.add(new ArrayList<>());
                volcano[i] = -1;
                time[i][0] = MAX_V;
                time[i][1] = MAX_V;
            }
            for (int i = 1; i <= n - 1; ++i) {
                s = new StringTokenizer(br.readLine());
                int v = Integer.parseInt(s.nextToken());
                int to = Integer.parseInt(s.nextToken());
                edges.get(v).add(to);
                edges.get(to).add(v);
            }

            int l = 0, r = 0, cur;
            volcano[1] = 0;
            q[r] = 1;
            while (l <= r) {
                cur = q[l];
                for (int i = 0; i < edges.get(cur).size(); ++i) {
                    int to = edges.get(cur).get(i);
                    if (volcano[to] == -1) {
                        volcano[to] = volcano[cur] + 1;
                        q[++r] = to;
                    }
                }
                l++;
            }

            l = 0; r = 0;
            time[start][0] = 0;
            lives[start][0] = 1;
            volcanoD[start][0] = volcano[start];
            q[r] = start; qT[r] = 0;
            int ans = 0;
            int qL = 0; byte qtL = 0;
            boolean shouldRevert = false;
            int livesHere = MAX_V;
            int livesRevert = 0;
            int volcanoTime = 0, volcanoDist = 0;
            while (l <= r) {
                qL = q[l];
                qtL = qT[l];
                // update the response.
                if (prev[l] != 0) {
                    if (lives[qL][qtL] < 1 && qtL == 1 && volcanoD[qL][qtL] > 2) {
                        lives[qL][qtL] += 2;
                        time[qL][qtL] += 2;
                        volcanoD[qL][qtL] -= 2;
                    } else if (lives[qL][qtL] <= 0) {
                        l++;
                        continue;
                    }
                }

                if (volcanoD[qL][qtL] < 1 && lives[qL][qtL] > 0) {
                    ans = Math.max(ans, time[qL][qtL]);
                }

                if (lives[qL][qtL] <= 0 || volcanoD[qL][qtL] <= 0) {
                    l++;
                    continue;
                }

                if ((qtL == 1 || lives[qL][qtL] > 0) && volcanoD[qL][qtL] > 0) {
                    shouldRevert = false;
                    if ((lives[qL][qtL] < 1 || (lives[qL][qtL] == 1 && st[qL] == -1)) && qtL == 1 && volcanoD[qL][qtL] > 2) {
                        lives[qL][qtL] += 2;
                        time[qL][qtL] += 2;
                        volcanoD[qL][qtL] -= 2;
                        shouldRevert = true;
                    }
                    livesHere = MAX_V;
                    livesRevert = 0;
                    if (prev[l] > 0 && st[prev[l]] == -1 && st[qL] == -1) {
                        livesHere = time[qL][qtL] + lives[qL][qtL] - 1;
                        if (qtL == 1) {
                            int moreLives = (volcanoD[qL][qtL] > 2) ? (volcanoD[qL][qtL] >> 1) : 0;
                            livesRevert = (2 * moreLives);
                            livesHere += (2 * moreLives);
                            time[qL][qtL] += livesRevert;
                        }
                    }
                    volcanoTime = time[qL][qtL];
                    if (l > 0) {
                        volcanoDist = 0;
                        if (volcano[prev[l]] < volcano[qL]) {
                            volcanoDist = volcano[qL] - time[qL][qtL];
                            volcanoTime = (volcanoDist % 2 == 0) ? (volcano[qL] - 1) : volcano[qL];
                        } else {
                            volcanoDist = volcano[prev[l]] - (time[qL][qtL] + 1);
                            volcanoTime = (volcanoDist % 2 == 0) ? (volcano[prev[l]] - 1) : volcano[prev[l]];
                        }
                        ans = Math.max(ans, Math.min(livesHere, volcanoTime));
                    }
                    time[qL][qtL] -= livesRevert;
                    if (shouldRevert) {
                        lives[qL][qtL] -= 2;
                        time[qL][qtL] -= 2;
                        volcanoD[qL][qtL] += 2;
                    }
                }

                boolean isLoop = (st[qL] == 1 && st[prev[l]] == 1);
                for (int i = 0; i < edges.get(qL).size(); ++i) {
                    int to = edges.get(qL).get(i);
                    if (qtL == 0 && to == prev[l] && time[to][1] == MAX_V && isLoop) {
                        time[to][1] = time[qL][qtL] + 1;
                        lives[to][1] = lives[qL][qtL] + st[qL];
                        volcanoD[to][1] = Math.min(volcanoD[qL][qtL], volcano[to] - time[to][1]);
                        q[++r] = to;
                        qT[r] = 1;
                        prev[r] = qL;
                    }
                    if (to != prev[l] && time[to][qtL] == MAX_V){
                        time[to][qtL] = time[qL][qtL] + 1;
                        lives[to][qtL] = lives[qL][qtL] + st[qL];
                        volcanoD[to][qtL] = Math.min(volcanoD[qL][qtL], volcano[to] - time[to][qtL]);
                        q[++r] = to;
                        qT[r] = qtL;
                        prev[r] = qL;
                    }
                    if (qtL == 0 && volcanoD[prev[l]][qtL] > 2 && isLoop && time[qL][1] == MAX_V) {
                         time[qL][1] = time[qL][qtL] + 2;
                         lives[qL][1] = lives[qL][qtL] + 2;
                         volcanoD[qL][1] = Math.min(volcanoD[qL][qtL], volcano[qL] - time[qL][1]);
                         q[++r] = qL;
                         qT[r] = 1;
                         prev[r] = prev[l];
                    }
                }
                l++;
            }
            System.out.println(ans);
        }
    }

}
