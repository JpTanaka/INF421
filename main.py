from graph import Graph

def read_file(file_name):
    with open(file_name, "r") as file:
        first_line = file.readline()
        n, m = map(int, first_line.split())
        edges = []
        for i in range(m):
            edges.append([int(x) for x in file.readline().split()])

        return [n, edges]


if __name__=="__main__":
    print(read_file("/home/nakatinha/repos/INF421/tests/tests/itineraries.0.in"))