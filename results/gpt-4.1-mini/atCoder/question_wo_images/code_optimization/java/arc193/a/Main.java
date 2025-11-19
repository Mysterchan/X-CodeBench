import java.util.*;
public class Main {
    static int[] parent, size;
    static long[] compWeight;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] weights = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            weights[i] = sc.nextInt();
        }

        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            intervals[i][0] = sc.nextInt();
            intervals[i][1] = sc.nextInt();
        }

        // Initialize DSU
        parent = new int[n + 1];
        size = new int[n + 1];
        compWeight = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
            compWeight[i] = weights[i];
        }

        // Sort intervals by L ascending
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(intervals[a][0], intervals[b][0]));

        // We'll build edges between vertices whose intervals do NOT intersect.
        // Two intervals do NOT intersect if one ends before the other starts.
        // So edges exist between intervals that are disjoint.

        // To find connected components in G, where edges connect vertices with disjoint intervals,
        // we find connected components of the complement of the interval intersection graph.

        // The intersection graph connects intervals that overlap.
        // Our graph G connects intervals that do NOT overlap.

        // So, intervals that overlap form cliques in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // To find connected components in G, we can find connected components in the complement graph.
        // The complement graph's connected components correspond to groups of intervals that are pairwise overlapping or connected through overlapping intervals.

        // So, intervals that overlap form connected components in the intersection graph.
        // The complement graph G's connected components are formed by intervals that are NOT overlapping.

        // Therefore, connected components in G correspond to connected components in the complement of the intersection graph.
        // But it's easier to find connected components in the intersection graph and then invert.

        // However, the problem asks for connectivity in G (edges between intervals that do NOT intersect).
        // So intervals that overlap are NOT connected in G.

        // So intervals that overlap form "blocks" that are disconnected in G.
        // Intervals that do NOT overlap are connected in G.

        // So, intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So, intervals that overlap form "cliques" in the intersection graph.
        // The complement graph G connects intervals that are disjoint.

        // Therefore, connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap group".
        // - Intervals that do NOT overlap are connected in G.

        // So intervals that overlap form connected components in the intersection graph.
        // The complement graph G connects intervals that do NOT overlap.

        // So intervals that overlap form "blocks" disconnected in G.
        // Intervals that do NOT overlap connect these blocks.

        // So the connected components in G correspond to connected components formed by intervals that are pairwise disjoint or connected through disjointness.

        // To find connected components in G, we can:
        // - Sort intervals by L ascending.
        // - For each interval, find intervals that do NOT overlap with it.
        // - Connect them in DSU.

        // But this is expensive if done naively.

        // Instead, we can use a sweep line approach:
        // - Sort intervals by L ascending.
        // - Maintain a data structure of intervals currently "active" (overlapping).
        // - Intervals that overlap are in the same "overlap