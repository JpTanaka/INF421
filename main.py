from graph import Graph
import time

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
        return [n, m, edges, queries, n_queries]

def time_v1():
    for i in range(3):
        test_0 = read_file(f"/home/nakatinha/repos/INF421/tests/tests/itineraries.{i}.in")
        
        grafo = Graph(test_0[0], test_0[1])
        grafo.addEdges(test_0[2])
        t1 = time.perf_counter()
        for j in test_0[3]:
            grafo.itineraries_v1(j[0], j[1])
        t2 = time.perf_counter()
        print(i, t2-t1)

def time_v2():
    for i in range(10):   
        test_0 = read_file(f"/home/nakatinha/repos/INF421/tests/tests/itineraries.{i}.in")
        grafo = Graph(test_0[0], test_0[1])
        grafo.addEdges(test_0[2])
        t1 = time.perf_counter()
        
        answer, times = grafo.itineraries_v2(test_0[3])
        t2 = time.perf_counter()
        print(i, {**times, "n":test_0[0], "m":test_0[1], "total_time": t2-t1})


def time_v3():
    for i in range(10):
        test_0 = read_file(f"/home/nakatinha/repos/INF421/tests/tests/itineraries.{i}.in")
        grafo = Graph(test_0[0], test_0[1])
        grafo.addEdges(test_0[2])

        t1 = time.perf_counter()
        grafo.itineraries_v3(test_0[3])
        t2 = time.perf_counter()
        print(i, t2-t1)



if __name__=="__main__":
    # time_v1()
    time_v2()
    # time_v3()
    