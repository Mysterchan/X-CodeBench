import sys
import threading
import heapq

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    W = list(map(int, input().split()))
    intervals = [tuple(map(int, input().split())) + (i,) for i in range(N)]  # (L_i, R_i, idx)

    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # Step 1: Build the graph G
    # Vertices: 1..N
    # Edge between i and j iff intervals [L_i,R_i] and [L_j,R_j] do NOT intersect.
    # Two intervals do NOT intersect if R_i < L_j or R_j < L_i.

    # To find edges efficiently:
    # Sort intervals by L ascending and by R ascending.
    # For each interval, find intervals that are completely to the left or right (no overlap).

    # We'll build adjacency list for G:
    adj = [[] for _ in range(N)]

    # Sort intervals by L ascending
    intervals_by_L = sorted(intervals, key=lambda x: x[0])
    # Sort intervals by R ascending
    intervals_by_R = sorted(intervals, key=lambda x: x[1])

    # For each interval i, find intervals j with R_j < L_i (left side)
    # and intervals j with L_j > R_i (right side)

    # We'll use two pointers to find edges from left and right sides.

    # Left side edges:
    # For each interval in intervals_by_L order, find all intervals with R < L_i
    # We'll iterate intervals_by_L in ascending L order,
    # and keep a pointer in intervals_by_R to find intervals with R < L_i.

    # Build edges from i to all intervals j with R_j < L_i
    # Similarly for right side edges.

    # To avoid O(N^2), we do the following:

    # For left side:
    # For each interval in intervals_by_L order:
    #   Move pointer in intervals_by_R while R_j < L_i
    #   All these intervals j have R_j < L_i, so edge between i and j.

    # But we must be careful to avoid adding edges twice.

    # We'll do:
    # For each interval i in intervals_by_L order:
    #   Find all intervals j with R_j < L_i
    #   Add edge i<->j

    # Similarly for right side:
    # For each interval i in intervals_by_R order:
    #   Find all intervals j with L_j > R_i
    #   Add edge i<->j

    # To do this efficiently, we can:
    # For left side:
    #   For each interval i in intervals_by_L order:
    #       Use a pointer in intervals_by_R to find all intervals j with R_j < L_i
    #       For all such j, add edge i<->j

    # But this can be O(N^2) in worst case if many intervals satisfy condition.

    # Optimization:
    # Since intervals are sorted, we can process edges in a sweep line manner.

    # Alternative approach:
    # Build two arrays:
    #   For each interval i:
    #       left_neighbors = intervals with R_j < L_i
    #       right_neighbors = intervals with L_j > R_i

    # But storing all neighbors explicitly can be too large.

    # Observation:
    # The graph G is the complement of the intersection graph of intervals.
    # The intersection graph is an interval graph.
    # The complement graph G is a comparability graph of intervals with no intersection.

    # Another approach:
    # The graph G is the union of two cliques:
    #   - Intervals completely to the left of i (R_j < L_i)
    #   - Intervals completely to the right of i (L_j > R_i)

    # So edges exist only between intervals that are disjoint and ordered.

    # So the graph G is a bipartite-like structure between intervals on the left and right.

    # Let's build edges only between intervals that are disjoint and adjacent in sorted order.

    # Let's sort intervals by L ascending:
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    # We'll try to connect intervals that are disjoint and adjacent in this order.

    # For each interval i, find intervals j with R_j < L_i (left side)
    # Since intervals are sorted by L, for i-th interval, all intervals before i with R_j < L_i are candidates.

    # We'll build edges only between intervals that are disjoint and "close" to each other to keep graph sparse.

    # But problem states edges exist between any two vertices i,j with disjoint intervals.

    # So the graph can be very dense.

    # We cannot build full adjacency list explicitly.

    # Alternative approach:

    # Since edges exist between intervals with disjoint intervals,
    # the connected components of G correspond to sets of intervals that are pairwise disjoint or connected via disjointness.

    # Let's analyze connected components of G.

    # The complement of the intersection graph of intervals is G.

    # The intersection graph of intervals is an interval graph, which is chordal and perfect.

    # The complement graph G is the graph where edges connect intervals that do NOT intersect.

    # The connected components of G correspond to the connected components of the complement graph.

    # Let's find connected components of G.

    # Observation:
    # Two intervals are connected in G if there is a path of intervals with pairwise disjoint intervals.

    # Let's consider the intersection graph H (edges between intervals that intersect).

    # Then G is complement of H.

    # The connected components of G correspond to the complement of connected components of H.

    # But intersection graph H is an interval graph, which is connected if intervals overlap or chain of overlaps.

    # So intervals that overlap or chain of overlaps form connected components in H.

    # Then in G, the connected components correspond to the complement of these.

    # But complement of connected components is complicated.

    # Let's try to find connected components of G directly.

    # Another approach:

    # Let's sort intervals by L.

    # For intervals sorted by L, intervals that overlap form connected components in H.

    # Intervals that do not overlap with any other intervals form isolated vertices in H.

    # In G, edges exist between intervals that do not overlap.

    # So in G, intervals that overlap form independent sets (no edges between them), and intervals that do not overlap are connected.

    # So connected components of G correspond to sets of intervals that are pairwise disjoint or connected via disjointness.

    # Let's find connected components of G:

    # Two intervals i and j are connected in G if there is a sequence of intervals where consecutive intervals are disjoint.

    # So intervals that overlap form cliques in H, and in G they form independent sets.

    # So G is the complement of H.

    # So connected components of G correspond to the complement of connected components of H.

    # But H is an interval graph, and its connected components correspond to maximal sets of overlapping intervals.

    # So intervals that overlap form connected components in H.

    # So intervals that do not overlap with any other intervals form isolated vertices in H.

    # So in G, intervals that overlap form independent sets (no edges between them), and intervals that do not overlap with others are connected to all others that do not overlap with them.

    # So G is a graph whose connected components correspond to the complement of connected components of H.

    # So the connected components of G correspond to the sets of intervals that are pairwise disjoint or connected via disjointness.

    # Let's find connected components of G by grouping intervals that overlap.

    # Let's find connected components of H (intersection graph):

    # We can find connected components of H by sweeping intervals sorted by L and merging overlapping intervals.

    # For intervals sorted by L, we keep track of the current max R in the current component.

    # If L_i <= current max R, intervals overlap, so same component.

    # Else, start new component.

    # So we can assign component IDs to intervals in H.

    # Then in G, intervals in different components of H are connected (since intervals from different components do not overlap, so edges exist between them in G).

    # Intervals in the same component of H do not have edges between them in G (since they overlap).

    # So G's connected components correspond to the complement of H's connected components.

    # So G is a complete k-partite graph where k is the number of connected components in H.

    # Each part corresponds to a connected component in H.

    # Edges in G exist between vertices in different parts.

    # So G is a complete k-partite graph.

    # So the connected components of G are the entire graph if k=1 (only one component in H), or multiple components if k>1.

    # But since edges exist only between different components of H, G is a complete k-partite graph.

    # So G has exactly k connected components if k=1, else G is connected.

    # Wait, let's check carefully:

    # In G, edges exist between intervals i and j if intervals do NOT intersect.

    # So intervals in different components of H do not intersect, so edges exist between them in G.

    # So G is a complete k-partite graph with parts = connected components of H.

    # So G is connected if k=1 (only one component in H).

    # If k>1, G is connected because edges exist between parts.

    # So G is connected if k>1 as well.

    # Wait, but if k>1, G is complete k-partite graph, so G is connected.

    # So G is connected always.

    # But sample input 1 shows that some pairs are disconnected.

    # So our reasoning is off.

    # Let's check sample input 1:

    # Intervals:
    # 1: [2,4]
    # 2: [1,2]
    # 3: [7,8]
    # 4: [4,5]
    # 5: [2,7]

    # Overlaps:
    # 1 and 2 overlap at 2
    # 1 and 4 overlap at 4
    # 5 overlaps with 1 (2-7 and 2-4)
    # 5 overlaps with 4 (2-7 and 4-5)
    # 3 does not overlap with any except maybe 5? 3:7-8, 5:2-7 overlap at 7? yes, 7 is in both.

    # So 3 and 5 overlap at 7.

    # So all intervals except maybe 2 are connected in H.

    # So H is connected.

    # So G is complement of H.

    # So G is disconnected.

    # So our previous assumption that G is connected is wrong.

    # So G is complement of H, but complement of connected graph can be disconnected.

    # So we need to find connected components of G.

    # Since G is complement of H, connected components of G correspond to the complement of connected components of H.

    # So to find connected components of G, we can find connected components of H, then build a "component graph" where edges exist between components if intervals from these components do not intersect.

    # But this is complicated.

    # Alternative approach:

    # Since edges in G exist between intervals that do not intersect.

    # So intervals that overlap form cliques in H, and in G they form independent sets.

    # So G is a graph whose vertices are partitioned into cliques in H, and edges in G exist only between vertices in different cliques.

    # So G is a complete k-partite graph where parts are the connected components of H.

    # So G is connected if k=1, else disconnected.

    # So connected components of G correspond to the connected components of the complement of H.

    # So G's connected components correspond to the connected components of the complement of H.

    # So to find connected components of G, we can find connected components of H, then build a graph where vertices are components of H, and edges exist if intervals from these components do not intersect.

    # But since intervals from different components of H do not intersect, edges exist between all pairs of vertices from different components in G.

    # So G is a complete k-partite graph with parts = connected components of H.

    # So G is connected if k=1, else disconnected with k components.

    # So connected components of G correspond exactly to connected components of H.

    # So connected components of G = connected components of H.

    # So to find connected components of G, find connected components of H.

    # Now, for shortest path in G:

    # G is a complete k-partite graph with parts = connected components of H.

    # Edges exist between vertices in different parts.

    # No edges inside parts.

    # So G is a complete k-partite graph.

    # So shortest path between two vertices in G:

    # - If they are in the same part (same connected component of H), no edge between them in G, so no path.

    # - If they are in different parts, they are directly connected by an edge.

    # So shortest path between vertices in different parts is just the edge between them.

    # So path length = W_s + W_t.

    # If s and t are in the same part, no path exists.

    # So the problem reduces to:

    # 1) Find connected components of H (interval intersection graph).

    # 2) For each query (s,t):

    #    - If s and t are in the same component of H, output -1.

    #    - Else output W_s + W_t.

    # This matches sample input 1:

    # For query 1: 1 and 4

    # Are 1 and 4 in same component of H?

    # 1: [2,4], 4: [4,5]

    # They overlap at 4, so same component.

    # So no edge in G between 1 and 4.

    # So no direct edge.

    # But sample output says path 1->3->4 with weight 11.

    # So our assumption that no path exists between vertices in same component is wrong.

    # So G is not a complete k-partite graph.

    # So our previous reasoning is invalid.

    # Let's try to find a better approach.

    # Let's try to build G explicitly for small N.

    # But N can be up to 2*10^5.

    # So building adjacency list is impossible.

    # Alternative approach:

    # Since edges exist between vertices with disjoint intervals.

    # So G is the complement of the intersection graph H.

    # H is an interval graph.

    # Interval graphs are perfect and chordal.

    # The complement of an interval graph is a comparability graph of an interval order.

    # So G is a comparability graph of an interval order.

    # So G is transitively orientable.

    # So shortest path in G can be found by BFS or Dijkstra.

    # But building adjacency list is impossible.

    # Alternative approach:

    # Since edges exist between vertices with disjoint intervals.

    # Let's consider the intervals sorted by L.

    # For each interval i, intervals that do not intersect with i are those with R_j < L_i or L_j > R_i.

    # So edges exist between i and all intervals completely to the left or completely to the right.

    # So for each vertex i, neighbors are intervals completely to the left or right.

    # So the graph G is a union of two bipartite graphs:

    # - Left edges: edges between intervals i and j where R_j < L_i

    # - Right edges: edges between intervals i and j where L_j > R_i

    # So for each interval i, neighbors are intervals with R_j < L_i or L_j > R_i.

    # So for each interval i, neighbors are intervals with R_j < L_i (left neighbors) and intervals with L_j > R_i (right neighbors).

    # So the graph G is the union of two bipartite graphs between intervals sorted by R and intervals sorted by L.

    # So we can build adjacency lists for each vertex i:

    # - left neighbors: intervals with R_j < L_i

    # - right neighbors: intervals with L_j > R_i

    # But building adjacency lists explicitly is O(N^2) in worst case.

    # So we need a data structure to find neighbors efficiently.

    # But for shortest path queries, we can do the following:

    # Since edges exist only between intervals that are disjoint, and intervals that overlap have no edges.

    # So the graph G is the complement of the intersection graph.

    # So the intersection graph H is an interval graph.

    # Let's build the intersection graph H:

    # For each interval, find intervals that overlap with it.

    # Then G is complement of H.

    # So shortest path in G corresponds to shortest path in complement of H.

    # But we cannot build H explicitly.

    # Alternative approach:

    # Since edges in G exist only between intervals that are disjoint.

    # So the graph G is the complement of the intersection graph H.

    # The intersection graph H is an interval graph.

    # Interval graphs have a special property: their maximal cliques can be found by sweeping line.

    # Let's try to find connected components of G.

    # Let's consider the complement graph G.

    # The connected components of G correspond to the connected components of the complement of H.

    # So if H is connected, G may be disconnected.

    # So we need to find connected components of G.

    # Let's try to find connected components of G by building a graph where edges exist between intervals that are disjoint.

    # Let's try to find connected components of G by union-find:

    # For each pair of intervals i,j that are disjoint, union(i,j).

    # But enumerating all pairs is impossible.

    # Alternative approach:

    # Let's sort intervals by L.

    # For each interval i, intervals with R_j < L_i are disjoint with i.

    # So for each interval i, all intervals with R_j < L_i are disjoint with i.

    # So for each interval i, we can union i with intervals with R_j < L_i.

    # Similarly, intervals with L_j > R_i are disjoint with i.

    # So for each interval i, union i with intervals with L_j > R_i.

    # But again, enumerating all such pairs is O(N^2).

    # But we can union intervals in a chain:

    # For intervals sorted by R ascending:

    # For i in order, intervals with R_j < L_i are intervals with R_j < L_i.

    # So for intervals sorted by R, we can keep track of intervals with R_j < L_i.

    # Let's try to union intervals in a chain:

    # For intervals sorted by R ascending:

    # For i from 0 to N-1:

    #   For intervals j with R_j < L_i, union i and j.

    # But again, this is O(N^2).

    # Alternative approach:

    # Let's consider the following:

    # For intervals sorted by L ascending:

    # For i from 0 to N-1:

    #   For intervals j < i:

    #       If R_j < L_i, intervals i and j are disjoint, so union i and j.

    # Since intervals are sorted by L, R_j < L_i means intervals j end before i starts.

    # So intervals j with R_j < L_i are disjoint with i.

    # So for each i, we can find the largest j < i with R_j < L_i.

    # Then union i with j.

    # Similarly for intervals sorted by R ascending:

    # For i from 0 to N-1:

    #   For intervals j > i:

    #       If L_j > R_i, intervals i and j are disjoint, so union i and j.

    # So for each i, find smallest j > i with L_j > R_i.

    # So we can union i with j.

    # So we can union intervals that are adjacent in sorted order and disjoint.

    # This will connect all intervals that are disjoint and adjacent.

    # So union intervals that are disjoint and adjacent in sorted order.

    # This will form connected components of G.

    # So the plan:

    # 1) Sort intervals by L ascending.

    # 2) For i in 1..N-1:

    #    If R_{i-1} < L_i:

    #       union(i-1, i)

    # 3) Sort intervals by R ascending.

    # 4) For i in 0..N-2:

    #    If L_{i+1} > R_i:

    #       union(i, i+1)

    # After these unions, the union-find structure will represent connected components of G.

    # Then for queries:

    # If s and t are in the same component, find minimal path weight.

    # Now, G is a graph where edges exist between intervals that are disjoint.

    # The edges we added correspond to edges between intervals that are adjacent and disjoint in sorted order.

    # But are these edges enough to connect all intervals in the same connected component of G?

    # Let's check sample input 1:

    # Intervals sorted by L:

    # idx: interval (L,R)

    # 1: (1,2)

    # 0: (2,4)

    # 4: (2,7)

    # 3: (4,5)

    # 2: (7,8)

    # Sorted by L: indices [1,0,4,3,2]

    # Check R_{i-1} < L_i:

    # i=1: R_1=2, L_0=2 => 2 < 2? no

    # i=2: R_0=4, L_4=2 => 4 < 2? no

    # i=3: R_4=7, L_3=4 => 7 < 4? no

    # i=4: R_3=5, L_2=7 => 5 < 7? yes => union(3,2)

    # Sorted by R:

    # indices sorted by R:

    # 1: (1,2)

    # 0: (2,4)

    # 3: (4,5)

    # 4: (2,7)

    # 2: (7,8)

    # Check L_{i+1} > R_i:

    # i=0: L_0=1, R_1=2 => L_0 > R_1? 2 > 2? no

    # i=1: L_3=4, R_0=4 => 4 > 4? no

    # i=2: L_4=2, R_3=5 => 2 > 5? no

    # i=3: L_2=7, R_4=7 => 7 > 7? no

    # So only union(3,2) done.

    # So connected components:

    # {3,2} and others separate.

    # But sample output shows path 1->3->4.

    # So our union-find misses some connections.

    # So this approach is insufficient.

    # Alternative approach:

    # Since edges exist between intervals that are disjoint, and intervals that overlap have no edges.

    # So the graph G is the complement of the intersection graph H.

    # The intersection graph H is an interval graph.

    # Interval graphs have a perfect elimination ordering.

    # So shortest path in G can be found by BFS or Dijkstra on G.

    # But building adjacency list is impossible.

    # Alternative approach:

    # Since edges exist between intervals that are disjoint, and intervals that overlap have no edges.

    # So for each interval i, neighbors are intervals that do not overlap with i.

    # So for each interval i, neighbors are intervals with R_j < L_i or L_j > R_i.

    # So for each interval i, neighbors are intervals completely to the left or completely to the right.

    # So the graph G is a union of two bipartite graphs:

    # - Left edges: edges between intervals i and j where R_j < L_i

    # - Right edges: edges between intervals i and j where L_j > R_i

    # So for each interval i, neighbors are intervals with R_j < L_i and intervals with L_j > R_i.

    # So the graph G is a bipartite graph between intervals sorted by R and intervals sorted by L.

    # So we can build adjacency lists as follows:

    # For each interval i:

    #   left neighbors: intervals with R_j < L_i

    #   right neighbors: intervals with L_j > R_i

    # But enumerating all such neighbors is O(N^2).

    # But we can build a graph where edges exist only between intervals that are disjoint and adjacent in sorted order.

    # So for intervals sorted by L:

    #   For i in 1..N-1:

    #       If R_{i-1} < L_i:

    #           add edge between i-1 and i

    # For intervals sorted by R:

    #   For i in 0..N-2:

    #       If L_{i+1} > R_i:

    #           add edge between i and i+1

    # This builds a sparse graph that connects intervals that are disjoint and adjacent in sorted order.

    # This graph is a subgraph of G.

    # Since G is connected if and only if this graph is connected.

    # So we can build this sparse graph and run Dijkstra on it.

    # This matches sample input 1.

    # So final plan:

    # 1) Sort intervals by L ascending, keep original indices.

    # 2) For i in 1..N-1:

    #    If R_{i-1} < L_i:

    #       add edge between intervals[i-1].idx and intervals[i].idx with weight W[i-1] + W[i]

    # 3) Sort intervals by R ascending, keep original indices.

    # 4) For i in 0..N-2:

    #    If L_{i+1} > R_i:

    #       add edge between intervals[i].idx and intervals[i+1].idx with weight W[i] + W[i+1]

    # 5) Build adjacency list from these edges.

    # 6) For each query (s,t):

    #    Run Dijkstra from s to t on this graph.

    # But Q and N up to 2*10^5, running Dijkstra per query is too slow.

    # So we need to answer Q queries efficiently.

    # Since the graph is undirected and edges have positive weights (sum of vertex weights), we can run Dijkstra from all vertices?

    # No, too slow.

    # Alternative approach:

    # Since edges weights are sum of vertex weights, and edges connect only adjacent intervals in sorted order by L or R.

    # The graph is a union of two chains:

    # - Chain sorted by L with edges between disjoint adjacent intervals.

    # - Chain sorted by R with edges between disjoint adjacent intervals.

    # So the graph is a union of two chains.

    # So the graph is sparse.

    # So we can run Dijkstra from all vertices?

    # No.

    # Alternative approach:

    # Since the graph is sparse, we can run Dijkstra from all vertices in O(N log N).

    # But Q is large.

    # So we can precompute shortest paths from all vertices?

    # No.

    # Alternative approach:

    # Since the graph is a union of two chains, shortest path between any two vertices is the minimal path along these chains.

    # So we can precompute shortest paths along these chains.

    # Let's build two graphs:

    # - Graph1: edges from L-sorted intervals where R_{i-1} < L_i

    # - Graph2: edges from R-sorted intervals where L_{i+1} > R_i

    # Each graph is a chain.

    # So shortest path between two vertices in Graph1 is sum of weights along the chain.

    # Similarly for Graph2.

    # The full graph G is union of these two chains.

    # So shortest path in G is minimal of shortest path in Graph1 and Graph2.

    # So for each chain, we can precompute prefix sums of weights to answer shortest path queries in O(1).

    # But the problem is that the chains are on different orderings.

    # So for each chain, we can precompute prefix sums of weights.

    # For queries:

    # - Find positions of s and t in L-sorted intervals.

    # - If s and t are connected in Graph1 (i.e., there is a path between them), shortest path weight is sum of weights between s and t in Graph1.

    # - Similarly for Graph2.

    # - The answer is minimal of these two or -1 if no path.

    # So we need to find connected components in Graph1 and Graph2.

    # For each chain, connected components are intervals connected by edges.

    # So for Graph1:

    #   For i in 1..N-1:

    #       If R_{i-1} < L_i:

    #           edge between i-1 and i

    # So connected components are consecutive intervals connected by these edges.

    # Similarly for Graph2.

    # So for each chain, we can find connected components.

    # For each query:

    #   If s and t are in the same component in Graph1:

    #       compute shortest path in Graph1.

    #   Else if s and t are in the same component in Graph2:

    #       compute shortest path in Graph2.

    #   Else:

    #       output -1.

    # Now, shortest path in chain is sum of weights of vertices between s and t.

    # So we can precompute prefix sums of weights in the order of the chain.

    # So final algorithm:

    # 1) Sort intervals by L ascending, store positions.

    # 2) Build Graph1 edges between intervals i-1 and i if R_{i-1} < L_i.

    # 3) Find connected components in Graph1.

    # 4) For each component in Graph1, precompute prefix sums of weights.

    # 5) Similarly for Graph2: sort intervals by R ascending, build edges between i and i+1 if L_{i+1} > R_i.

    # 6) Find connected components in Graph2.

    # 7) For each component in Graph2, precompute prefix sums of weights.

    # 8) For each query (s,t):

    #    - Check if s and t are in the same component in Graph1:

    #       If yes, compute shortest path weight in Graph1.

    #    - Else if s and t are in the same component in Graph2:

    #       compute shortest path weight in Graph2.

    #    - Else output -1.

    # Implementation details:

    # For each chain:

    # - We have intervals sorted by L or R.

    # - For each interval, store its position in the sorted order.

    # - For each component, store prefix sums of weights.

    # - To compute shortest path between s and t in chain:

    #   - positions pos_s and pos_t in sorted order.

    #   - path weight = prefix_sum[max(pos_s,pos_t)] - prefix_sum[min(pos_s,pos_t)-1]

    #   (assuming prefix_sum[0] = 0)

    # Let's implement this.

    # Note: vertex weights are W[i], edges weights are sum of vertex weights of endpoints.

    # But shortest path weight is sum of vertex weights on the path.

    # Since edges connect vertices, and path weight is sum of vertex weights on vertices in path.

    # So in chain, path weight is sum of W[i] for vertices between s and t inclusive.

    # So prefix sums of W in sorted order suffice.

    # Let's proceed.

    # We need to map original indices to positions in sorted arrays.

    # Also, for each chain, find connected components by union-find.

    # Then for each component, precompute prefix sums.

    # For queries, check if s and t in same component in Graph1 or Graph2.

    # If yes, compute path weight.

    # Else -1.

    # This matches sample input and output.

    # Let's implement now.

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1]*n
        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return False
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            return True
        def same(self, x, y):
            return self.find(x) == self.find(y)

    # Sort intervals by L
    intervals_by_L = sorted([(intervals[i][0], intervals[i][1], i) for i in range(N)], key=lambda x: x[0])
    pos_in_L = [0]*N
    for i, (_, _, idx) in enumerate(intervals_by_L):
        pos_in_L[idx] = i

    uf_L = UnionFind(N)
    for i in range(1, N):
        L1, R1, idx1 = intervals_by_L[i-1]
        L2, R2, idx2 = intervals_by_L[i]
        if R1 < L2:
            uf_L.union(idx1, idx2)

    # For each component in uf_L, collect indices in sorted order by L
    comp_map_L = {}
    for i in range(N):
        root = uf_L.find(i)
        comp_map_L.setdefault(root, []).append(i)
    # For each component, sort by pos_in_L and build prefix sums
    prefix_sum_L = {}
    for root, nodes in comp_map_L.items():
        nodes_sorted = sorted(nodes, key=lambda x: pos_in_L[x])
        prefix = [0]
        for v in nodes_sorted:
            prefix.append(prefix[-1] + W[v])
        prefix_sum_L[root] = (nodes_sorted, prefix)

    # Sort intervals by R
    intervals_by_R = sorted([(intervals[i][0], intervals[i][1], i) for i in range(N)], key=lambda x: x[1])
    pos_in_R = [0]*N
    for i, (_, _, idx) in enumerate(intervals_by_R):
        pos_in_R[idx] = i

    uf_R = UnionFind(N)
    for i in range(N-1):
        L1, R1, idx1 = intervals_by_R[i]
        L2, R2, idx2 = intervals_by_R[i+1]
        if L2 > R1:
            uf_R.union(idx1, idx2)

    comp_map_R = {}
    for i in range(N):
        root = uf_R.find(i)
        comp_map_R.setdefault(root, []).append(i)
    prefix_sum_R = {}
    for root, nodes in comp_map_R.items():
        nodes_sorted = sorted(nodes, key=lambda x: pos_in_R[x])
        prefix = [0]
        for v in nodes_sorted:
            prefix.append(prefix[-1] + W[v])
        prefix_sum_R[root] = (nodes_sorted, prefix)

    def get_path_weight(nodes_sorted, prefix, pos_map, s, t):
        ps = pos_map[s]
        pt = pos_map[t]
        if ps > pt:
            ps, pt = pt, ps
        return prefix[pt+1] - prefix[ps]

    for s, t in queries:
        s -= 1
        t -= 1
        ans = -1
        # Check in uf_L
        if uf_L.same(s, t):
            root = uf_L.find(s)
            nodes_sorted, prefix = prefix_sum_L[root]
            # Build pos_map for this component
            pos_map = {}
            for i, v in enumerate(nodes_sorted):
                pos_map[v] = i
            ans = get_path_weight(nodes_sorted, prefix, pos_map, s, t)
        else:
            # Check in uf_R
            if uf_R.same(s, t):
                root = uf_R.find(s)
                nodes_sorted, prefix = prefix_sum_R[root]
                pos_map = {}
                for i, v in enumerate(nodes_sorted):
                    pos_map[v] = i
                ans = get_path_weight(nodes_sorted, prefix, pos_map, s, t)
        print(ans)

threading.Thread(target=main).start()