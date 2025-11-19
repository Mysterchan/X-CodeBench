import java.awt.event.KeyListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {

    static ArrayList<Integer>[] adj;
    static ArrayList<Integer> sizes;
    static int stop;

    public static void main(String[] args) throws IOException {
        BufferedReader br;
        PrintWriter out;
        StringTokenizer st;
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        for(int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            adj = new ArrayList[N];
            for(int i = 0; i < N; i++) {
                adj[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for(int i = 1; i < N; i++) {
                adj[Integer.parseInt(st.nextToken()) - 1].add(i);
            }

            sizes = new ArrayList<>();
            int numZeros = K;
            int numOnes = N - K;
            stop = -1;
            ArrayList<int[]> rootList = new ArrayList<>(Arrays.asList(new int[] {0, -1}));
            traverse(rootList, 0);

            if (stop == -1) {
                stop = Integer.MAX_VALUE;
            }

            boolean atBottomPossible = true;

            int numZerosChange = numZeros;
            int numOnesChange = numOnes;
            if (numZerosChange >= sizes.get(stop)) {
                numZerosChange -= sizes.get(stop);
                for (int i = stop - 1; i >= 0; i--) {
                    int amount = sizes.get(i);
                    boolean useZeros = numZerosChange < numOnesChange;

                    if (useZeros) {
                        if (numZerosChange >= amount) {
                            numZerosChange -= amount;
                        } else if (numOnesChange >= amount) {
                            numOnesChange -= amount;
                        } else {
                            atBottomPossible = false;
                            break;
                        }
                    } else {
                        if (numOnesChange >= amount) {
                            numOnesChange -= amount;
                        } else if (numZerosChange >= amount) {
                            numZerosChange -= amount;
                        } else {
                            atBottomPossible = false;
                            break;
                        }
                    }
                }
            } else {
                atBottomPossible = false;
            }

            if(atBottomPossible) {
                out.println(stop + 1);
            } else {
                atBottomPossible = true;

                numZerosChange = numZeros;
                numOnesChange = numOnes;
                if (numOnesChange >= sizes.get(stop)) {
                    numOnesChange -= sizes.get(stop);
                    for (int i = stop - 1; i >= 0; i--) {
                        int amount = sizes.get(i);
                        boolean useZeros = numZerosChange < numOnesChange;

                        if (useZeros) {
                            if (numZerosChange >= amount) {
                                numZerosChange -= amount;
                            } else if (numOnesChange >= amount) {
                                numOnesChange -= amount;
                            } else {
                                atBottomPossible = false;
                                break;
                            }
                        } else {
                            if (numOnesChange >= amount) {
                                numOnesChange -= amount;
                            } else if (numZerosChange >= amount) {
                                numZerosChange -= amount;
                            } else {
                                atBottomPossible = false;
                                break;
                            }
                        }
                    }
                } else {
                    atBottomPossible = false;
                }

                if (atBottomPossible) {
                    out.println(stop + 1);
                } else {
                    out.println(stop);
                }
            }
        }

        out.close();
    }

    static void traverse(ArrayList<int[]> nodes, int depth) {
        sizes.add(nodes.size());
        boolean moveOn = true;
        ArrayList<int[]> newNodes = new ArrayList<>();
        for(int[] n : nodes) {
            int node = n[0];
            int parent = n[1];

            int numChildren = 0;
            for (int e : adj[node]) {
                if (e != parent) {
                    numChildren++;
                    newNodes.add(new int[] {e, node});
                }
            }

            if (numChildren == 0) {
                moveOn = false;
                break;
            }
        }

        if (moveOn) {
            traverse(newNodes, depth + 1);
        } else {
            stop = depth;
        }
    }
}
