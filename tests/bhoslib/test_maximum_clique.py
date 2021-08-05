import unittest
import benchmark_graphs.bhoslib as bhoslib
import benchmark_graphs.parser.dimacs as dimacs
import networkx as nx


class MaximumClique(unittest.TestCase):

    def test_kexu_compliance(self):
        graph = bhoslib.maximum_clique_30()
        graph_kexu = dimacs.get_graph("tests.bhoslib.graphs", "kexu_frb30-15-1.clq")
        self.assertTrue(nx.is_isomorphic(graph, graph_kexu))

    def test_mc30(self):
        graph = bhoslib.maximum_clique_30()
        self.assertEqual(450, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(83198, graph.number_of_edges(), "Wrong number of edges")

    def test_mc35(self):
        graph = bhoslib.maximum_clique_35(instance=2)
        self.assertEqual(595, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(148868, graph.number_of_edges(), "Wrong number of edges")

    def test_mc40(self):
        graph = bhoslib.maximum_clique_40(instance=3)
        self.assertEqual(760, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(247325, graph.number_of_edges(), "Wrong number of edges")

    def test_mc45(self):
        graph = bhoslib.maximum_clique_45(instance=4)
        self.assertEqual(945, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(387491, graph.number_of_edges(), "Wrong number of edges")

    def test_mc50(self):
        graph = bhoslib.maximum_clique_50(instance=5)
        self.assertEqual(1150, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(580640, graph.number_of_edges(), "Wrong number of edges")

    def test_mc53(self):
        graph = bhoslib.maximum_clique_53(instance=4)
        self.assertEqual(1272, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(714048, graph.number_of_edges(), "Wrong number of edges")

    def test_mc56(self):
        graph = bhoslib.maximum_clique_56(instance=3)
        self.assertEqual(1400, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(869921, graph.number_of_edges(), "Wrong number of edges")

    def test_mc59(self):
        graph = bhoslib.maximum_clique_59(instance=2)
        self.assertEqual(1534, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(1049648, graph.number_of_edges(), "Wrong number of edges")

    def test_mc100(self):
        graph = bhoslib.maximum_clique_100(instance=1)
        self.assertEqual(4000, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(7425226, graph.number_of_edges(), "Wrong number of edges")

