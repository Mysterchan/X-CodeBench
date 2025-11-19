import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        List<Integer> answer = new ArrayList();
        Main j = new Main();
        Scanner scanner = new Scanner(System.in);
        int testCaseCount = scanner.nextInt();
        for (int i = 0; i < testCaseCount; ++i) {
            TestCase t = new TestCase(scanner);
            answer.addAll(t.paths);
        }
        answer.forEach(System.out::println);
    }

    static class TestCase {
        Tree tree;
        List<Integer> paths = new ArrayList();
        public TestCase(Scanner scanner) {
            tree = new Tree();
            // read vertices
            scanner.nextLine();
            int verticeCount = scanner.nextInt();
            for (int v = 0; v < verticeCount; ++v) {
                int initStatus = scanner.nextInt();
                tree.addNode(initStatus > 0);
            }
            // read edges
            for (int n = 0; n < verticeCount - 1; ++n) {
                scanner.nextLine();
                int id1 = scanner.nextInt();
                int id2 = scanner.nextInt();
                tree.addEdge(id1, id2);
            }
            paths.add(tree.query());
            // read queries
            int queryCount = scanner.nextInt();
            for (int q = 0; q < queryCount; ++q) {
                scanner.nextLine();
                int queriedNodeIndex = scanner.nextInt();
                paths.add(tree.query(queriedNodeIndex));
            }
        }
    }

    static class Tree {
        int lastId = 0;
        List<TreeNode> nodes = null;

        public Tree() {
            nodes = new ArrayList<>();
        }

        public void addNode(boolean hasMonster) {
            TreeNode node = new TreeNode(++lastId, hasMonster);
            nodes.add(node);
        }

        public void addEdge(int id1, int id2) {
            TreeNode n1 = nodes.get(id1 - 1);
            TreeNode n2 = nodes.get(id2 - 1);
            n1.addBranch(n2);
            n2.addBranch(n1);
        }

        public TreeNode getNode(int id) {
            return nodes.get(id - 1);
        }

        public int query() {
            return nodes.get(0).query(nodes.get(0));
        }

        public int query(int id) {
            TreeNode fromNode = nodes.get(id-1);
            int newPathCount = nodes.get(id-1).query();
            // revert update
            while(fromNode.parent!=null) {
                fromNode = fromNode.parent;
                int originalPathCount = fromNode.subPathCount;
                fromNode.subPathCount = fromNode.branches.stream().mapToInt(n -> n.subPathCount).sum();
                if(fromNode.subPathCount==0 && fromNode.hasMonster) fromNode.subPathCount = 1;
                if(originalPathCount==fromNode.subPathCount) // no change
                    return nodes.get(0).subPathCount;
            }
            return fromNode.subPathCount;
        }
    }

    static class TreeNode {
        int id = 0;
        TreeNode parent = null;
        List<TreeNode> branches = new ArrayList<>();
        int subPathCount = 0;
        boolean hasMonster = false;

        public TreeNode(int id, boolean hasMonster) {
            this.id = id;
            this.hasMonster = hasMonster;
        }

        public int query() { return query(null); }
        public int query(TreeNode p) {
            if(p==null) hasMonster = !hasMonster;
            else if(id>1) {
                parent = p;
                branches.remove(p);
            }
            else parent = null;
            subPathCount = 0;
            for(TreeNode n : branches) {
                subPathCount += n.query(p!=null ? this : null);
            }
            if(subPathCount==0 && hasMonster) subPathCount = 1;
            return subPathCount;
        }

        public void addBranch(TreeNode child) {
            if (branches.contains(child)) return;
            branches.add(child);
            child.parent = this;
        }
    }
}
