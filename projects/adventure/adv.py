from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}
roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}], 12: [(4, 6), {'w': 1, 'e': 13}], 13: [(5, 6), {'w': 12, 'n': 14}], 14: [(5, 7), {'s': 13}], 15: [(2, 6), {'e': 1, 'w': 16}], 16: [(1, 6), {'n': 17, 'e': 15}], 17: [(1, 7), {'s': 16}]}


world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()

player = Player("Name", world.startingRoom)

# Fill this out
traversalPath = []

visited = {}
dirs_dict = {}
q = Queue()
s = Stack()

## initialize visited with first room
initial_dirs = {'n': '?', 's': '?', 'e': '?', 'w': '?'}
visited[0] = initial_dirs

print(f"visited[0] : {visited[0]}")

# we begin our journey with a bfs 
# for a room with a direction to '?'

def bfs_maze(starting_room):
    ## returns shortest path to 
    # room with directional '?'

    ## create empty queue
    ## enqueue path to starting_room
    q = Queue()
    bfs_visited = set()
    q.enqueue([starting_room])

    while q.size() > 0:
        ## dequeue first path
        path = q.dequeue()
        ## get last room from path
        vertex = path[-1]

        # if room hasn't been visited
        if vertex not in bfs_visited:
            ## check if target of search
            for room in visited[vertex]:
                if visited[vertex][room] == '?':
                    # return path
                    return path
            # mark as visited
            bfs_visited.add(vertex)

            ## add paths to neighbors to queue
            for neighbor in visited[vertex]:
                # create a copy of the path
                list_copy = path.copy()
                ## append neighbor
                list_copy.append(visited[vertex][neighbor])
                q.enqueue(list_copy)
        # if do not find target return None
        return None






# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
