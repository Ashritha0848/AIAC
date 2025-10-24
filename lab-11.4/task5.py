class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Add vertex to adjacency list if not already present
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        # Add an edge from u to v (undirected)
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        # Breadth-First Search Traversal starting from 'start'
        visited = set()                # Track visited vertices
        queue = []                     # Use list as a queue for BFS
        result = []

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)      # Dequeue a vertex
            result.append(vertex)
            # Visit all the adjacent vertices
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return result

    def dfs_iterative(self, start):
        # Iterative Depth-First Search Traversal
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()            # Take the last inserted vertex
            if vertex not in visited:
                result.append(vertex)
                visited.add(vertex)
                # Push adjacent nodes to stack (could reverse for traditional order)
                for neighbor in reversed(self.adj_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

    def dfs_recursive(self, start):
        # Recursive Depth-First Search helper
        def dfs_helper(vertex, visited, result):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor, visited, result)
        
        visited = set()
        result = []
        dfs_helper(start, visited, result)
        return result

    def __str__(self):
        return '\n'.join([f"{vertex}: {neighbors}" for vertex, neighbors in self.adj_list.items()])


def main():
    print("Graph Traversal (Adjacency List)")
    print("Commands: add_edge u v, bfs start, dfs_iter start, dfs_rec start, show, quit")
    graph = Graph()
    while True:
        cmd = input("Enter command: ").strip()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == "quit":
            print("Exiting graph test.")
            break
        elif parts[0] == "add_edge" and len(parts) == 3:
            u, v = parts[1], parts[2]
            graph.add_edge(u, v)
            print(f"Edge added between {u} and {v}")
        elif parts[0] == "bfs" and len(parts) == 2:
            start = parts[1]
            if start not in graph.adj_list:
                print(f"Vertex {start} not in graph.")
                continue
            traversal = graph.bfs(start)
            print("BFS Traversal:", traversal)
        elif parts[0] == "dfs_iter" and len(parts) == 2:
            start = parts[1]
            if start not in graph.adj_list:
                print(f"Vertex {start} not in graph.")
                continue
            traversal = graph.dfs_iterative(start)
            print("Iterative DFS Traversal:", traversal)
        elif parts[0] == "dfs_rec" and len(parts) == 2:
            start = parts[1]
            if start not in graph.adj_list:
                print(f"Vertex {start} not in graph.")
                continue
            traversal = graph.dfs_recursive(start)
            print("Recursive DFS Traversal:", traversal)
        elif parts[0] == "show":
            print("Adjacency List:")
            print(graph)
        else:
            print("Unknown or invalid command.")

if __name__ == "__main__":
    main()
