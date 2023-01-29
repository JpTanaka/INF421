from graph import Graph

def read_file(file_name):
    with open(file_name, "r") as file:
        graph_line = file.readline()
        n, m = map(int, graph_line.split())
        edges = []
        for _ in range(m):
            edges.append([int(x) for x in file.readline().split()])


        queries = []
        n_queries = int(file.readline())
        for _ in range(n_queries):
            queries.append([int(x) for x in file.readline().split()])
        return [n, m, edges, queries]


if __name__=="__main__":
    test_0 = read_file("/home/nakatinha/repos/INF421/tests/tests/itineraries.0.in")

    