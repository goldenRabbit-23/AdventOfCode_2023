import sys
import networkx as nx


def main():
    data = open(sys.argv[1]).read().splitlines()
    G = nx.Graph()

    for line in data:
        parts = line.split(': ')
        head = parts[0]
        connections = parts[1].split()
        for tail in connections:
            G.add_edge(head, tail)

    cut_size, partition = nx.stoer_wagner(G)

    if cut_size == 3:
        print(len(partition[0]) * len(partition[1]))


if __name__ == "__main__":
    main()
