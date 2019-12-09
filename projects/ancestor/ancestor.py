from graph import Graph
from util import Stack, Queue


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

    q = Queue()
    visited = set()
    p1 = [starting_node]
    q.enqueue(p1)

    ## keep track of all paths
    all_paths = [p1]

    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1] # last node visited in path
        if vertex not in visited:
            ## add to path
            visited.add(vertex)
        
        for next_vertex in g.vertices[vertex]:
            ## create new paths
            new_path = list(path)
            new_path.append(next_vertex)
            all_paths.append(new_path)
            q.enqueue(new_path)


    print(f"all_paths : {all_paths}")
    return None

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
