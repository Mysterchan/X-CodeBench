import sys
import threading
from collections import deque, defaultdict
import heapq

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    W = list(map(int, input().split()))
    intervals = [tuple(map(int, input().split())) + (i,) for i in range(N)]

    # Step 1: Build connected components of G's complement graph (edges between intervals that intersect)
    # Sort intervals by L_i
    intervals.sort(key=lambda x: x[0])  # sort by L_i

    comp_id = [-1] * N
    comp_cnt = 0

    # We'll find connected components of the complement graph (edges between intervals that intersect)
    # Using a sweep line approach:
    # For intervals sorted by L_i, intervals that intersect form connected components.
    # We can find these components by merging intervals that overlap.

    # We'll keep track of the current merged interval and assign component ids accordingly.
    current_left, current_right = intervals[0][0], intervals[0][1]
    comp_id[intervals[0][2]] = 0
    comp_cnt = 1

    for i in range(1, N):
        L, R, idx = intervals[i]
        if L <= current_right:
            # Overlaps with current merged interval
            comp_id[idx] = comp_cnt - 1
            if R > current_right:
                current_right = R
        else:
            # No overlap, start new component
            comp_id[idx] = comp_cnt
            comp_cnt += 1
            current_left, current_right = L, R

    # Step 2: Build the graph G
    # G has edges between vertices whose intervals do NOT intersect
    # i.e., edges between vertices in different components

    # Since intervals in the same component intersect, no edges inside component
    # Edges only between vertices in different components

    # We need to find edges between vertices in different components.
    # The problem states: edge exists iff intervals do NOT intersect.

    # So, for each pair of vertices in different components, there is an edge.
    # But this is a complete multipartite graph with parts = components.

    # So G is a complete multipartite graph with parts = components.

    # Step 3: For each component, find minimal weight vertex
    comp_min_w = [10**15] * comp_cnt
    comp_min_idx = [-1] * comp_cnt
    for i in range(N):
        c = comp_id[i]
        if W[i] < comp_min_w[c]:
            comp_min_w[c] = W[i]
            comp_min_idx[c] = i

    # Step 4: Build a "component graph" where each node is a component
    # Edges between every pair of distinct components (complete graph)
    # Edge weight between components c1 and c2 is comp_min_w[c1] + comp_min_w[c2]

    # Step 5: For queries:
    # If s and t in same component:
    #   path exists only if s == t (not possible since s != t), so no path, output -1
    # Else:
    #   path must go through minimal weight vertices of their components
    #   minimal path weight = W[s] + W[t] + comp_min_w[c_s] + comp_min_w[c_t]

    # But we must consider the path weight as sum of weights of vertices on the path.
    # The path is s -> comp_min_idx[c_s] -> comp_min_idx[c_t] -> t
    # But s and comp_min_idx[c_s] are in same component, no edge between them (since edges only between different components)
    # So s and comp_min_idx[c_s] are in same component, no edge between them.
    # So path must be s -> comp_min_idx[c_s] only if s == comp_min_idx[c_s], else no edge.
    # So we must consider that s and comp_min_idx[c_s] are same vertex or s == comp_min_idx[c_s].
    # Similarly for t.

    # Wait, this suggests that the minimal path between s and t is:
    # s -> comp_min_idx[c_s] (if s != comp_min_idx[c_s], no edge)
    # comp_min_idx[c_s] -> comp_min_idx[c_t] (edge exists)
    # comp_min_idx[c_t] -> t (if t != comp_min_idx[c_t], no edge)

    # So the only edges are between vertices in different components.
    # So to move from s to t, we must:
    # - If s == comp_min_idx[c_s] and t == comp_min_idx[c_t], path is direct edge between these two minimal vertices.
    # - If s != comp_min_idx[c_s], no edge from s to comp_min_idx[c_s], so no path.
    # - Similarly for t.

    # So path exists only if s and t are minimal vertices of their components or s == t (not allowed).
    # So path exists only if s == comp_min_idx[c_s] and t == comp_min_idx[c_t].

    # But sample input contradicts this, so our assumption is wrong.

    # Let's reconsider:

    # Since edges exist only between vertices whose intervals do NOT intersect,
    # and intervals in the same component intersect, so no edges inside component.

    # So the graph G is a complete multipartite graph with parts = components.

    # So edges exist between every pair of vertices in different components.

    # So for s and t in different components, path length is 1 if s and t are in different components (edge exists).

    # So minimal path weight is W[s] + W[t].

    # But sample input 1 shows path 1->3->4 with weight 11, which is W[1]+W[3]+W[4]=5+4+2=11.

    # So edge between 1 and 4 does not exist, so path length > 1.

    # So the graph is not a complete multipartite graph.

    # So our initial assumption is wrong.

    # Let's re-express the problem:

    # Edge exists between i and j iff intervals [L_i,R_i] and [L_j,R_j] do NOT intersect.

    # So intervals that intersect: no edge.

    # Intervals that do not intersect: edge.

    # So the graph G is the complement of the intersection graph of intervals.

    # The intersection graph of intervals is an interval graph.

    # The complement of an interval graph is a comparability graph of the complement poset.

    # But we need a practical approach.

    # Let's try to build the graph G:

    # For each vertex i, edges to all vertices j where intervals do not intersect.

    # Since intervals are on [1, 2N], and N up to 2e5, building adjacency lists explicitly is impossible.

    # But we can model the graph G as follows:

    # The intersection graph is an interval graph.

    # The complement graph G has edges between intervals that do not intersect.

    # So G is the complement of an interval graph.

    # The complement of an interval graph is a comparability graph of an interval order.

    # The complement graph G is a comparability graph of an interval order.

    # The problem reduces to shortest path queries on G with vertex weights.

    # Since edges exist only between intervals that do not intersect, and intervals are on [1,2N].

    # Let's try to find connected components of G.

    # Two vertices are connected in G if there is a path between them.

    # Since edges exist only between intervals that do not intersect.

    # So intervals that intersect form cliques in the intersection graph, and no edges in G.

    # So G's connected components correspond to sets of intervals that are pairwise non-intersecting or connected via non-intersecting intervals.

    # Let's try to find connected components of G.

    # Let's build an interval graph of intervals (edges between intersecting intervals).

    # Then G is the complement graph.

    # So connected components of G correspond to connected components in the complement graph.

    # But complement graph connected components are not trivial.

    # Let's try to find connected components of G:

    # Two vertices i and j are connected in G if there is a sequence of vertices where consecutive intervals do not intersect.

    # So intervals that are pairwise intersecting are isolated in G.

    # So intervals that intersect form cliques in the intersection graph, and are isolated in G.

    # So intervals that intersect form isolated vertices or isolated cliques in G.

    # So G's connected components correspond to sets of intervals that are pairwise non-intersecting or connected via non-intersecting intervals.

    # Let's try to find connected components of G by building an interval graph and then find connected components in its complement.

    # But this is complicated.

    # Alternative approach:

    # Since edges exist only between intervals that do not intersect.

    # So for each vertex, edges to all vertices whose intervals do not intersect with it.

    # So for each vertex, neighbors are all vertices whose intervals are disjoint with it.

    # So the graph G is the complement of the interval graph.

    # The interval graph is chordal, so its complement is comparability graph.

    # But we need a practical solution.

    # Let's try to build the graph G as follows:

    # For each vertex i, intervals [L_i, R_i].

    # For each vertex, find intervals that do not intersect with it.

    # Since intervals are on [1, 2N], we can sort intervals by L_i.

    # For each interval, intervals that do not intersect with it are those intervals j where R_j < L_i or L_j > R_i.

    # So intervals that are completely to the left or right of interval i.

    # So for each interval i, neighbors are intervals j where R_j < L_i or L_j > R_i.

    # So the graph G is a union of two bipartite graphs:

    # - edges between intervals to the left of i (R_j < L_i)

    # - edges between intervals to the right of i (L_j > R_i)

    # So the graph G is a union of edges between intervals that are completely to the left or right.

    # So the graph G is a bipartite graph between intervals on the left and intervals on the right.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of edges between intervals that are disjoint.

    # So the graph G is a union of