graph = Graph.get_graph_from_layer(path_to_ecological_corridor)  #with open source library QGIS

graph.compute_cut_nodes()   #implemented in Java, with open source library JGraphT

print(graph.count_nodes)      #6995
print(graph.count_edges)      #17464
print(graph.count_cut_nodes)  #569

virtual_cut_nodes = dict()

for parent_node in graph.nodes:
    graph_i = Graph.get_graph_without_node(graph, parent_node)
    graph_i.compute_cut_nodes()

    if graph_i.count_cut_nodes > graph.count_cut_nodes:
        set_a = graph_i.cut_nodes
        set_b = graph.cut_nodes

        virtual_cut_nodes[parent_node] = set_a.difference(set_b) #save in dictionary the parent node and his children

print(virtual_cut_nodes)