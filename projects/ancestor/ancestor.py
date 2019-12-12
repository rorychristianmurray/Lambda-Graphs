from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    ## instantiate graph
    g = Graph()
    
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
        ## while inverting the tree

        g.add_edge(i[1], i[0])
    
    # print(f"g.vertices : {g.vertices}")

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
    
    longest_path = 0
    parent_of_longest_path = None
    for path in all_paths:
        if len(path) == longest_path:
            check_id = path[-1]
            if check_id < parent_of_longest_path:
                parent_of_longest_path = check_id
        if len(path) > longest_path:
            longest_path = len(path)
            parent_of_longest_path = path[-1]
    
    # print(f"longest_path : {longest_path}")
    # print(f"parent_of_longest_path : {parent_of_longest_path}")

    # print(f"all_paths : {all_paths}")

    if parent_of_longest_path is starting_node:
        parent_of_longest_path = -1


    return parent_of_longest_path

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 11))
