import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class ps1_student {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int trials = in.nextInt();
		for (int a = 0; a < trials; a++) {
			List<Integer>[] nodes = new ArrayList[in.nextInt()];
			for (int b = 0; b < nodes.length; b++) {
				nodes[b] = new ArrayList<>();
			}
			int edges = in.nextInt();
			int startNode = in.nextInt()-1;
			int maxDist = in.nextInt();
			for (int b = 0; b < edges; b++) {
				int from = in.nextInt()-1;
				int to = in.nextInt()-1;
				nodes[from].add(to);
				nodes[to].add(from);
			}
			System.out.println(getComponents(nodes) + " " + getNodesFromStart(nodes, startNode, maxDist));
		}
		in.close();
	}
	
	//Iterative DFS to find components
	public static int getComponents(List<Integer>[] adjacencyList) {
		boolean[] visitedList = new boolean[adjacencyList.length];
		int nextCheck = 0;
		Stack<Integer> check = new Stack<>();
		int components = 0;
		while (nextCheck < visitedList.length) {
			check.push(nextCheck);
			nextCheck++;
			while (!check.isEmpty()) {
				Integer subject = check.pop();
				visitedList[subject.intValue()] = true;
				for (Integer i: adjacencyList[subject]) {
					if (!visitedList[i])
						check.push(i);
				}
			}
			components++;
			while (nextCheck < visitedList.length && visitedList[nextCheck])
				nextCheck++;
		}
		return components;
	}
	
	//Iterative BFS to find nearby nodes
	public static int getNodesFromStart(List<Integer>[] adjacencyList, int startNode, int distance) {
		Queue<Integer> check = new LinkedList<>();
		check.offer(startNode);
		int[] dists = new int[adjacencyList.length];
		Arrays.fill(dists, -1);
		dists[startNode] = 0;
		int nodes = 0;
		
		while (!check.isEmpty()) {
			Integer subject = check.poll();
			nodes++;
			if (dists[subject] < distance) {
				for (Integer i: adjacencyList[subject]) {
					if (dists[i] < 0) {
						dists[i] = dists[subject]+1;
						check.offer(i);
					}
				}
			}
		}
		return nodes;
	}
}
