import importlib_resources
import networkx as nx


def import_graph(path, filename):
    if filename.endswith(".b"):
        return binary_import_graph(path, filename)
    else:
        return ascii_import_graph(path, filename)


def ascii_import_graph(path, filename):
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
        if line_type == 'c':
            # comment line -> print it and ignore it...
            print(line)
        elif line_type == 'p':
            # Check the format
            assert (tokens[1] == "edge"), "Unknown format - expected 'edge'"
            nodes = int(tokens[2])
            edges = int(tokens[3])
        elif line_type == 'e':
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


def binary_import_graph(path, filename):
    """ Based on http://archive.dimacs.rutgers.edu/pub/challenge/graph/translators/binformat/ANSI/README.binformat:
    BINARY FORMAT for storing a graph of N vertices
    -----------------------------------------------

    The file consists of 3 blocks:

        First Line
        Preamble
        Binary Block (The rest of the file)

        The First Line contains an integer (%d, say #) describing the
        length of the proceeding preamble.

        The a Preamble consists of # characters, and contains possibly
    some comments following the ascii format plus a line
    describing the number of vertices and edges in the graph.
    (In "p type Num_vertices Num_edges" format).

        The Binary Block contains the lower triangular part of the
    vertex-vertex adjacency matrix of the graph. Each row of the matrix is
    stored as sequence of bits, where the j'th bit is 1 if the edge (i,j)
    is in the graph otherwise the bit is 0. (Note that i >= j)
    """

    nodes = int()
    edges = int()
    graph = nx.Graph()

    length_of_preamble = -1
    bytes_read_from_preamble = 0
    i = 0
    parse_binary = False
    source = importlib_resources.files(path).joinpath(filename)
    line = bytearray()
    matrix_row = bytearray()
    bytes_per_row = 1
    bytes_currently_added_to_row = 0
    for byte in source.read_bytes():
        if parse_binary:
            # Parse the "Binary Block"
            matrix_row.append(byte)
            bytes_currently_added_to_row = bytes_currently_added_to_row + 1
            if bytes_currently_added_to_row == bytes_per_row:
                # We have read a full row of the adjacency matrix => add edges (for the i'th node) to the graph
                add_edges(graph, i, matrix_row)
                # Start a new row for the next node
                matrix_row = bytearray()
                bytes_currently_added_to_row = 0
                i = i + 1
                if i % 8 == 0:
                    # We need an additional row in the adjacency matrix in order to represent all edges
                    bytes_per_row = bytes_per_row + 1

        else:
            # Parse the ascii part ("First Line" and "Preamble" blocks)
            line.append(byte)
            if length_of_preamble > 0:
                # We are past the "First Line" block and reading from the preamble
                bytes_read_from_preamble = bytes_read_from_preamble + 1
            if bytes_read_from_preamble == length_of_preamble:
                # We're done reading the preamble => parse the binary section next
                parse_binary = True
            if byte == 0x0A: # We're at a newline
                if length_of_preamble == -1:
                    # ... and just read the "First Line" block (as the length of the preamble is as of yet unknown)
                    length_of_preamble = int(line.decode())
                else:
                    # Parse the line to see if it's a comment or a "problem" line
                    c_or_p_line = line.decode()
                    tokens = c_or_p_line.split()
                    line_type = tokens[0]
                    if line_type == 'c':
                        # comment line -> print it and ignore it...
                        print(c_or_p_line)
                    elif line_type == 'p':
                        # Check the format
                        assert (tokens[1] == "edge"), "Unknown format - expected 'edge'"
                        nodes = int(tokens[2])
                        edges = int(tokens[3])

                # Prepare to read the next line
                line = bytearray()

    assert(nodes == graph.number_of_nodes()), "Wrong number of nodes"
    assert(edges == graph.number_of_edges()), "Wrong number of edges"

    return graph


def bits(byte):
    for i in reversed(range(8)):
        yield (byte >> i) & 1


def add_edges(graph, i, matrix_row):
    j = 0
    current_byte = 0
    while j <= i:
        for b in bits(matrix_row[current_byte]):
            if b == 1:
                graph.add_edge(i, j)
            j = j + 1
        current_byte = current_byte + 1
