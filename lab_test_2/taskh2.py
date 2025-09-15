import heapq
import ast

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()
    queue = [(0, source)]

    # Step 2: Process nodes in priority order
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        # Step 3: Edge relaxation
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))

    return distances

if __name__ == "__main__":
    # Input: adjacency dict from console
    graph_input = input("Enter adjacency dict: ")
    graph = ast.literal_eval(graph_input)
    source = 'A'
    result = dijkstra(graph, source)
    print(result)