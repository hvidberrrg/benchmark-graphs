import networkx as nx
from benchmark_graphs.bhoslib.maximum_independent_set import *


def maximum_clique_30(instance=1):
    return nx.complement(maximum_independent_set_30(instance))


def maximum_clique_35(instance=1):
    return nx.complement(maximum_independent_set_35(instance))


def maximum_clique_40(instance=1):
    return nx.complement(maximum_independent_set_40(instance))


def maximum_clique_45(instance=1):
    return nx.complement(maximum_independent_set_45(instance))


def maximum_clique_50(instance=1):
    return nx.complement(maximum_independent_set_50(instance))


def maximum_clique_53(instance=1):
    return nx.complement(maximum_independent_set_53(instance))


def maximum_clique_56(instance=1):
    return nx.complement(maximum_independent_set_56(instance))


def maximum_clique_59(instance=1):
    return nx.complement(maximum_independent_set_59(instance))


def maximum_clique_100(instance=1):
    # This takes a few seconds, but compared to the time it takes to solve the MC problem it should be negligible :-)
    return nx.complement(maximum_independent_set_100(instance))

