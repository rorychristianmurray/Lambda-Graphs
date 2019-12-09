from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    ## instantiate graph
    g = Graph()

    # create set of keys
    # for i in ancestors:
    #     print(f"i[0] : {i[0]}")
    #     g.add_vertex(i[0])
    
    # build the graph
    for i in ancestors:
        ## for each tuple in the list
        ## add both as vertices and connect
        g.add_vertex(i[0])
        # g.add_vertex(i[1])
        # g.add_edge(i[0], i[1])
    
    for i in ancestors:
        ## for each tuple in the list
        ## add both as vertices and connect
        g.add_vertex(i[1])
    
    for i in ancestors:
        ## for each tuple in the list
        ## add both as vertices and connect
        g.add_edge(i[0], i[1])
    
    print(f"g.vertices : {g.vertices}")

    ## traverse the graph
    ## as traverse track path
    ## get length of paths
    ## return root of longest path
    ## if satisfy reqs
    return None

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
