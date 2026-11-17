from queue import Queue


class Graph:
    def __init__(self):
        self.vertexes = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertexes.keys():
            self.vertexes[vertex] = []
            self.vertex_count += 1

    def remove_vertex(self, vertex):
        if vertex in self.vertexes.keys():
            del self.vertexes[vertex]
            self.vertex_count -= 1

            for v in self.vertexes.keys():
                if vertex in self.vertexes[v]:
                    self.vertexes[v].remove(vertex)

    def add_neighbor(self, vertex, neighbor):
        if (
            vertex in self.vertexes.keys()
            and neighbor in self.vertexes.keys()
            and neighbor not in self.vertexes[vertex]
        ):
            self.vertexes[vertex].append(neighbor)

    def remove_neighbor(self, vertex, neighbor):
        if vertex in self.vertexes.keys() and neighbor in self.vertexes.keys():
            if neighbor in self.vertexes[vertex]:
                self.vertexes[vertex].remove(neighbor)

    def depth_search(self, start_vertex, end_vertex):
        if (
            start_vertex not in self.vertexes.keys()
            or end_vertex not in self.vertexes.keys()
        ):
            return f"Vertex {start_vertex} or {end_vertex} not found in the graph."

        self.verified = []
        stack = [start_vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in self.verified:
                if current_vertex == end_vertex:
                    return f"Vertex {end_vertex} found in the graph"

                self.verified.append(current_vertex)

                for neighbor in self.vertexes[current_vertex]:
                    if neighbor not in self.verified:
                        stack.append(neighbor)

    def width_search(self, start_vertex, end_vertex):
        if (
            start_vertex not in self.vertexes.keys()
            or end_vertex not in self.vertexes.keys()
        ):
            return f"Vertex {start_vertex} or {end_vertex} not found in the graph."

        self.verified = []
        queue = [start_vertex]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in self.verified:
                if current_vertex == end_vertex:
                    return f"Vertex {end_vertex} found in the graph"

                self.verified.append(current_vertex)

                for neighbor in self.vertexes[current_vertex]:
                    if neighbor not in self.verified:
                        queue.append(neighbor)

        return f"Vertex {end_vertex} not found in the graph."


MENU = """
===== GRAPH MENU =====
1 - Add vertex
2 - Remove vertex
3 - Add neighbor
4 - Remove neighbor
5 - Depth-first search (DFS)
6 - Breadth-first search (BFS)
7 - Show graph
0 - Exit
======================
"""


def main():
    graph = Graph()

    while True:
        print(MENU)
        option = input("Choose an option: ").strip()

        if option == "0":
            print("Goodbye!")
            break
        elif option == "1":
            graph.add_vertex(input("Vertex name: ").strip())

        elif option == "2":
            graph.remove_vertex(input("Vertex to remove: ").strip())

        elif option == "3":
            vertex = input("From vertex: ").strip()
            neighbor = input("To vertex: ").strip()
            graph.add_neighbor(vertex, neighbor)

        elif option == "4":
            vertex = input("From vertex: ").strip()
            neighbor = input("To vertex: ").strip()
            graph.remove_neighbor(vertex, neighbor)

        elif option == "5":
            start = input("Start vertex: ").strip()
            end = input("Target vertex: ").strip()
            print(graph.depth_search(start, end))

        elif option == "6":
            start = input("Start vertex: ").strip()
            end = input("Target vertex: ").strip()
            print(graph.width_search(start, end))

        elif option == "7":
            print(f"\nVertices: {graph.vertex_count}")

            for vertex, neighbors in graph.vertexes.items():
                print(f"{vertex} -> {neighbors}")
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
