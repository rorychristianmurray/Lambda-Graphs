"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # notation to add something
        # to a set
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else: 
            raise IndexError("That vertex does not exist")
    

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        ## Create an empty queue and enqueue starting vertex ID
        q =  Queue()
        q.enqueue(starting_vertex)

        ## Create empty Set to store visited vertices
        visited = set()

        ## While queue not empty
        while q.size() > 0:
            ## Dequeue first vertex
            v = q.dequeue()
            ## If not visited mark as visited
            if v not in visited:
                print(v)
                visited.add(v)
                ## add its neighbors to back of queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        ## Create an empty stack and enqueue starting vertex ID
        s =  Stack()
        s.push(starting_vertex)

        ## Create empty Set to store visited vertices
        visited = set()

        ## While stack not empty
        while s.size() > 0:
            ## Dequeue first vertex
            v = s.pop()
            ## If not visited mark as visited
            if v not in visited:
                print(v)
                visited.add(v)
                ## add its neighbors to back of queue
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
    
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        ## print visited node
        print(starting_vertex)

        ## add start vertex to visited set
        visited.add(starting_vertex)
        
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                # add to visited
                # call recursively on it
                self.dft_recursive(child_vertex, visited)

        # v = starting_vertex
        # if v not in self.visited:
        #     self.visited.add(v)
        #     print(f"recursive call v : {v}")
        #     for neighbor in self.vertices:
        #         self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        ## Create an empty queue and enqueue
        ## A PATH TO the starting vertex
        q = Queue()

        ## Create a Set to store visited vertices
        visited = set()

        q.enqueue([starting_vertex])

        ## while queue is not empty
        while q.size() > 0:
            ## dequeue the first PATH
            p = q.dequeue()
            ## grab the last vertex from the PATH
            v = p[-1]
            # if that vertex has not been visited
            if v not in visited:
                ## check if it is the target
                if v is destination_vertex:
                    ## if so return path
                    print(p)
                    return p
                ## mark as visited
                visited.add(v)

                for next_vert in self.vertices[v]:
                    ## create new paths
                    new_path = list(p)
                    new_path.append(next_vert)
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ## Create an empty stack and push
        ## A PATH TO the starting vertex
        s = Stack()
        path = [starting_vertex]
        s.push(path)

        ## Create a Set to store visited vertices
        visited = set()

        ## while stack is not empty
        while s.size() > 0:
            ## dequeue the first PATH
            p = s.pop()
            ## grab the last vertex from the PATH
            v = p[-1]
            # if that vertex has not been visited
            if v not in visited:
                ## check if it is the target
                if v is destination_vertex:
                    ## if so return path
                    print(p)
                    return p
                ## mark as visited
                visited.add(v)

                ## then add A PATH TO its neighbors 
                ## to the back of the queue
                for neighbor in self.vertices[v]:
                    print(f"dfs neighbor : {neighbor}")
                    ## copy the path
                    new_path = path
                    ## append neighbor to the back
                    new_path.append(neighbor)
                    print(f"new_path : {new_path}")
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        v = starting_vertex
        # store path that as first path
        self.path.append(v)

        ## check if vertex already visited
        if v not in self.visited:
            ## if hasn't been visited
            ## add to visited
            self.visited.add(v)
        ## check if target
            if v is destination_vertex:
                # if yes then print and return path
                print(f"dfs rec dest : {v}")
        
        ## recursively call fn
        ## for all neighbor vertices
        for i in self.vertices[v]:
            if i not in self.visited:
                dfs_recursive(i)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("\nstarting recursive DFT\n")
    graph.dft_recursive(1)
    print("\nending recursive DFT\n")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\nstarting breadth first search\n")
    print(graph.bfs(1, 6))
    print("\nending breadth first search\n")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))


# print(f"\ngraph.get_neighbors(7) : {graph.get_neighbors(7)}\n")
