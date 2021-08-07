import importlib_resources
import networkx as nx


def import_graph(path, filename):
    """Based on http://lcs.ios.ac.cn/~caisw/Resource/about_DIMACS_graph_format.txt

    DIMACS (Center for Discrete Mathematics and Theoretical Computer Science) defined
    a format for undirected graph, which has been used as a standard format for problems
    in undirected graphs. This format was also chosen for several DIMACS Computational
    Challenges.

    *Input Files*
    An input file contains all the information about an undirected graph. In this format,
    nodes are numbered from 1 up to n edges in the graph.

    Files are assumed to be well-formed and internally consistent: node identifier values
    are valid, nodes are defined uniquely, exactly m edges are defined, and so forth.

    *Comments*
     Comment lines give human-readable information about the file and are ignored by
     programs. Comment lines can appear anywhere in the file. Each comment line begins
     with a lower-case character c.

    c This is an example of a comment line.

    *Problem line*
    There is one problem line per input file. The problem line must appear before any node
    or arc descriptor lines. The problem line has the following format. p FORMAT NODES EDGES

    The lower-case character p signifies that this is the problem line. The FORMAT field is
    for consistency with the previous Challenge, and should contain the word ``edge''. The
    NODES field contains an integer value specifying n, the number of nodes in the graph.
    The EDGES field contains an integer value specifying m, the number of edges in the graph.

    *Edge Descriptors*
    There is one edge descriptor line for each edge the graph, each with the following format.
    Each edge (u,v) appears exactly once in the input file and is not repeated as (v,u).

    e u v

    The lower-case character e signifies that this is an edge descriptor line. For an edge (u,v)
    the fields u and v specify its endpoints.
    """

    nodes = int()
    edges = int()
    graph = nx.Graph()

    source = importlib_resources.files(path).joinpath(filename)
    for line in source.read_text().splitlines():
        # reimplement as 'match-case' when Python 3.10 is released
        tokens = line.split()
        line_type = tokens[0]
        if (line_type == 'c'):
            # comment line -> print it and ignore it...
            print(line)
        elif (line_type == 'p'):
            # Check the format
            assert (tokens[1] == "edge"), "Unknown format - expected 'edge'"
            nodes = int(tokens[2])
            edges = int(tokens[3])
        elif (line_type == 'e'):
            # Line representing an edge
            u = int(tokens[1])
            v = int(tokens[2])
            # DIMACS nodes are numbered from 1 up to n
            # We'll number them from 0 to n-1
            graph.add_edge(u-1, v-1)
        else:
            print("Unknown line type: " + line_type)

    assert(nodes == graph.number_of_nodes()), "Wrong number of nodes"
    assert(edges == graph.number_of_edges()), "Wrong number of edges"

    return graph
