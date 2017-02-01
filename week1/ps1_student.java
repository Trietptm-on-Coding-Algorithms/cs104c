import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;

public class ps1_student {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numTests = in.nextInt();
        for (int i = 0; i < numTests; i++) {
            int numNodes = in.nextInt();
            int numEdges = in.nextInt();
            int startNode = in.nextInt();
            int reach = in.nextInt();

            Graph graph = new Graph(numNodes);

            for (int j = 0; j < numEdges; j++) {
                graph.addEdge(in.nextInt(), in.nextInt());
            }

            System.out.println(graph.numCCs() + " " +
                    graph.numReachable(startNode, reach));
        }
    }

    public static class Graph {
        private ArrayList<HashSet<Integer>> graph;

        Graph(int numNodes) {
            graph = new ArrayList<>(numNodes + 1);
            for (int i = 0; i < numNodes + 1; i++) {
                graph.add(new HashSet<>());
            }
        }

        void addEdge(int u, int v) {
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        int numCCs() {
            int count = 0;
            LinkedList<Integer> toVisit = new LinkedList<>();
            HashSet<Integer> visited = new HashSet<>();

            for (int i = 1; i < graph.size(); i++) {
                if (visited.contains(i)) {
                    continue;
                }
                count++;
                toVisit.push(i);
                visited.add(i);

                while (!toVisit.isEmpty()) {
                    int nextNode = toVisit.pop();
                    for (int neighbor : graph.get(nextNode)) {
                        if (visited.contains(neighbor)) {
                            continue;
                        }
                        toVisit.push(neighbor);
                        visited.add(neighbor);
                    }
                }
            }

            return count;
        }

        int numReachable(int start, int reach) {
            int count = 0;
            HashSet<Integer> visited = new HashSet<>(); LinkedList<Tuple> toVisit = new LinkedList<>();

            toVisit.add(new Tuple(start, 0));
            visited.add(start);
            while (!toVisit.isEmpty()) {
                Tuple next = toVisit.remove();
                for (int neighbor : graph.get(next.node)) {
                    if (visited.contains(neighbor) || next.distance >= reach) {
                        continue;
                    }
                    toVisit.add(new Tuple(neighbor, next.distance + 1));
                    visited.add(neighbor);
                }
                count++;
            }
            return count;
        }
    }

    public static class Tuple {
        int node, distance;

        Tuple(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }
    }
}
