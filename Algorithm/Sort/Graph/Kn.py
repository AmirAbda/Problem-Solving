class K_n_Graph:
    """
    Definition: A complete graph K_n has every vertex connected to every other vertex by exactly one edge. This implies n(n-1)/2 unique edges.
    Properties:
    Number of edges: n(n-1)/2
    Degree of all vertices: n-1 (each vertex connects to n-1 others)
    No self-loops or parallel edges
    Applications: Network modeling, scheduling, routing problems, graph algorithms testing.
    """
    def __init__(self, num_vertices):
        if num_vertices < 1:
            raise ValueError("Number of vertices must be positive")
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self._build_edges()
        
    def _build_edges(self):
        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):  # to avoid double counting
                self.adj_matrix[i][j] = 1
                self.adj_matrix[j][i] = 1  # to validate the Undirect property
    
    def is_complete(self):
        return all(sum(row) == self.num_vertices - 1 for row in self.adj_matrix)
    
    def __str__(self):
        return f"Complete Graph K_{self.num_vertices} (Adjacency Matrix):\n" + \
               "\n".join(" ".join(str(x) for x in row) for row in self.adj_matrix)

# Test case
graph = K_n_Graph(5)
print(graph)
print(graph.is_complete())  # Should print True
