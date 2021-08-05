import unittest
import benchmark_graphs.bhoslib as bhoslib
import networkx as nx


class MaximumIndependentSet(unittest.TestCase):

    def test_mis30(self):
        graph = bhoslib.maximum_independent_set_30()
        self.assertEqual(450, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(17827, graph.number_of_edges(), "Wrong number of edges")

    def test_mis30_with_instance(self):
        graph = bhoslib.maximum_independent_set_30()
        graph_instance_1 = bhoslib.maximum_independent_set_30(instance=1)
        self.assertTrue(nx.is_isomorphic(graph, graph_instance_1))

    def test_mis30_instance_fail(self):
        with self.assertRaises(FileNotFoundError):
            graph = bhoslib.maximum_independent_set_30(instance=6)

    def test_mis35(self):
        graph = bhoslib.maximum_independent_set_35(instance=2)
        self.assertEqual(595, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(27847, graph.number_of_edges(), "Wrong number of edges")

    def test_mis40(self):
        graph = bhoslib.maximum_independent_set_40(instance=3)
        self.assertEqual(760, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(41095, graph.number_of_edges(), "Wrong number of edges")

    def test_mis45(self):
        graph = bhoslib.maximum_independent_set_45(instance=4)
        self.assertEqual(945, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(58549, graph.number_of_edges(), "Wrong number of edges")

    def test_mis50(self):
        graph = bhoslib.maximum_independent_set_50(instance=5)
        self.assertEqual(1150, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(80035, graph.number_of_edges(), "Wrong number of edges")

    def test_mis53(self):
        graph = bhoslib.maximum_independent_set_53(instance=4)
        self.assertEqual(1272, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(94308, graph.number_of_edges(), "Wrong number of edges")

    def test_mis56(self):
        graph = bhoslib.maximum_independent_set_56(instance=3)
        self.assertEqual(1400, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(109379, graph.number_of_edges(), "Wrong number of edges")

    def test_mis59(self):
        graph = bhoslib.maximum_independent_set_59(instance=2)
        self.assertEqual(1534, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(126163, graph.number_of_edges(), "Wrong number of edges")

    def test_mis100(self):
        graph = bhoslib.maximum_independent_set_100(instance=1)
        self.assertEqual(4000, graph.number_of_nodes(), "Wrong number of nodes")
        self.assertEqual(572774, graph.number_of_edges(), "Wrong number of edges")
