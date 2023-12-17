from collections import defaultdict, deque

class BFS:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

if __name__ == "__main__":
    try:
        vertices = int(input("Enter the number of vertices: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of vertices.")
        exit()

    g = BFS(vertices)

    try:
        edges = int(input("Enter the number of edges: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of edges.")
        exit()

    print("Enter the edges (format: source destination): ")
    for _ in range(edges):
        try:
            source, destination = map(int, input().split())
        except ValueError:
            print("Invalid input. Please enter valid integers for the edges.")
            exit()

        g.add_edge(source, destination)

    try: 
        start_vertex = int(input("Enter the starting vertex for BFS: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the starting vertex.")
        exit()

    print("Breadth First Traversal (starting from vertex {}):".format(start_vertex))
    g.bfs(start_vertex)
