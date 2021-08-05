import unittest
import benchmark_graphs.parser.dimacs as dimacs


class DimacsParserTest(unittest.TestCase):

    def setUp(self):
        self.path = "tests.parser.graphs"
        self.filename = "test_graph_in_dimacs_format"

    def test_parse_dimacs_graph_format(self):
        graph = dimacs.get_graph(self.path, self.filename)
        self.assertEqual(graph.number_of_nodes(), 3, "Wrong number of nodes")
        self.assertEqual(graph.number_of_edges(), 2, "Wrong number of edges")
