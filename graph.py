from queue import Queue
from set import Set


class Graph:
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.vertex = []
        self.adj_list = {}

    def __str__(self):
        res = ""
        for vertex in self.vertex:
            res += f"{vertex} -> "
            for neighbor in self.adj_list[vertex]:
                res += f"{neighbor} "
            res += "\n"
        return res

    def add_vertex(self, v):
        if not v in self.vertex:
            self.vertex.append(v)
            self.adj_list[v] = []

    def add_edge(self, a, b):
        self.add_vertex(a)
        self.add_vertex(b)

        self.adj_list[a].append(b)

        if not self.is_directed:
            self.adj_list[b].append(a)

    def bfs(self, element=None):
        queue = Queue()
        visited = Set()
        order = []

        if element is None:
            start = self.vertex[0]
        else:
            if element in self.vertex:
                start = element
            else:
                raise ValueError("Element not found")

        queue.enqueue(start)
        visited.add(start)

        while len(queue) > 0:
            current = queue.dequeue()
            order.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return order


def main():
    print("=== Undirected Graph ===")

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    print(graph)

    print("=" * 30)
    print()
    print("=== Directed Graph ===")

    directed_graph = Graph(is_directed=True)

    directed_graph.add_edge("A", "B")
    directed_graph.add_edge("A", "C")
    directed_graph.add_edge("C", "B")
    directed_graph.add_edge("B", "D")
    directed_graph.add_edge("D", "A")
    print(directed_graph)

    print("=" * 30)
    print()
    print("=== Visited Vertex ===")

    visited = graph.bfs("F")
    print(visited)


if __name__ == "__main__":
    main()
