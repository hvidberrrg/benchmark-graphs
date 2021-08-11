import unittest
import benchmark_graphs.parser.dimacs as dimacs
import networkx as nx


class DimacsParserTest(unittest.TestCase):

    def setUp(self):
        self.path = "tests.parser.graphs"

    def test_parse_dimacs_ascii_graph_format(self):
        filename = "test_graph_in_dimacs_format"
        graph = dimacs.import_graph(self.path, filename)
        self.assertEqual(graph.number_of_nodes(), 3, "Wrong number of nodes")
        self.assertEqual(graph.number_of_edges(), 2, "Wrong number of edges")

    def test_parse_dimacs_binary_graph_format(self):
        filename_bin = "DSJC125.1.col.b"
        graph = dimacs.import_graph(self.path, filename_bin)
        self.assertEqual(graph.number_of_nodes(), 125, "Wrong number of nodes")
        self.assertEqual(graph.number_of_edges(), 736, "Wrong number of edges")

    def test_parse_dimacs_graph_format(self):
        filename_bin = "DSJC125.1.col.b"
        graph_bin = dimacs.import_graph(self.path, filename_bin)
        filename_ascii = "DSJC125.1.col"
        graph_ascii = dimacs.import_graph(self.path, filename_ascii)
        self.assertTrue(nx.is_isomorphic(graph_ascii, graph_bin))
