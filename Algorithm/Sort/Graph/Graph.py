class Graph:
    """
    A simple graph class implementation using adjacency list representation.
    Atributes:
        verticres : A dictionary where keys are vertices and values or lists of connected vertices
        edges: A dictionary where keys are tuples of vertices (representing edges) and values are weights (optional).
    Methods:
        add_vertex: Adds a vertex to the graph
        add_edge: Adds an edge to the graph
        get_neighbors: Returns a list of neighbors of a vertex
    """
    def __init__(self):
        self.vertices={}
        self.edges={}
    def add_vertex(self,vertex):
        """"
        Adds a vertex to the graph
        Args: 
            vertex: The vertex to add
        """
        if vertex not in self.vertices: # check if it's already there or not
            self.vertices[vertex]=[]
    def add_edge(self,source,target,weight=None):
        """
        Adds an edge to the graph
        Args:
            source: The source vertex
            target: The target vertex
            weuight: the weight of the edge
        """
        if source not in self.vertices:
            self.add_vertex(source)
        if target not in self.vertices:
            self.add_edge(target)
        self.vertices[source].append(target)
        self.edges[(source,target)]=weight # represent the connection betwen two vertices using immutable tuples with a weight
    def get_neighbors(self,vertex):
        """
        Returns a list of neighbors of a vertex
        Args:
            vertex: The vertex fro which to get neighbors
        Returns:
            A list of neighbors of the vertex
        """
        if vertex not in self.vertices:
            return []
        return self.vertices[vertex]
# Example usage
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A", weight=3)

print(graph.get_neighbors("A"))  
print(graph.get_neighbors("B"))  
print(graph.get_neighbors("C"))  
print(graph.edges) 