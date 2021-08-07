import benchmark_graphs.parser.dimacs as dimacs

_graphs = "benchmark_graphs.bhoslib.graphs"
_mis = "mis"


def _get_frb_instance(frb, instance):
    # path is on the form: benchmark_graphs.bhoslib.graphs.frb30-15-mis
    # filename is on the form frb30-15-1.mis
    return dimacs.import_graph(_graphs + "." + frb + _mis, frb + str(instance) + "." + _mis)


def maximum_independent_set_30 (instance=1):
    return _get_frb_instance("frb30-15-", instance)


def maximum_independent_set_35 (instance=1):
    return _get_frb_instance("frb35-17-", instance)


def maximum_independent_set_40 (instance=1):
    return _get_frb_instance("frb40-19-", instance)


def maximum_independent_set_45 (instance=1):
    return _get_frb_instance("frb45-21-", instance)


def maximum_independent_set_50 (instance=1):
    return _get_frb_instance("frb50-23-", instance)


def maximum_independent_set_53 (instance=1):
    return _get_frb_instance("frb53-24-", instance)


def maximum_independent_set_56 (instance=1):
    return _get_frb_instance("frb56-25-", instance)


def maximum_independent_set_59 (instance=1):
    return _get_frb_instance("frb59-26-", instance)


def maximum_independent_set_100 (instance=1):
    return _get_frb_instance("frb100-40-", instance)