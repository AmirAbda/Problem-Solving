import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Graph {

    // Use HashMap for efficient vertex lookup
    private final Map<String, Set<String>> vertices = new HashMap<>();

    // Use HashMap for storing edges with weights
    private final Map<String, Map<String, Integer>> edges = new HashMap<>();

    // Use constructor for clear initialization
    public Graph() {
    }

    public void addVertex(String vertex) {
        if (!vertices.containsKey(vertex)) {
            vertices.put(vertex, new HashSet<>());
        }
    }

    public void addEdge(String source, String target, int weight) {
        addVertex(source);
        addVertex(target);

        vertices.get(source).add(target);

        // Store edges with weights for bidirectional access
        edges.putIfAbsent(source, new HashMap<>());
        edges.get(source).put(target, weight);

        // Store edges bidirectionally if undirected graph is needed
        if (isUndirected()) {
            edges.putIfAbsent(target, new HashMap<>());
            edges.get(target).put(source, weight);
        }
    }

    public Set<String> getNeighbors(String vertex) {
        return vertices.getOrDefault(vertex, new HashSet<>());
    }

    // Optional method for determining graph type
    public boolean isUndirected() {
        return false; // Adjust based on graph implementation
    }

    // Example usage
    public static void main(String[] args) {
    Graph graph = new Graph();
    graph.addVertex("A");
    graph.addVertex("B");
    graph.addVertex("C");
    graph.addEdge("A", "B", 0); 
    graph.addEdge("B", "C", 0);
    graph.addEdge("C", "A", 3);

    System.out.println(graph.getNeighbors("A"));  // Output: [B]
    System.out.println(graph.getNeighbors("B"));  // Output: [C] 
    System.out.println(graph.getNeighbors("C"));  // Output: [A]
    System.out.println(graph.edges);              // Output: {A={B=0, C=3}, B={C=0}, C={A=3}}
}
}