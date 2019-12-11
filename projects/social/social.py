import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}


    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # avg_friendships = total_friendships/num_users


        # Add users
        # call addUser() until number of users is num_users

        # Create random friendships
        # total_friendships = avg_friendships * num_users
        for i in range(numUsers):
            self.add_user(f"User {i+1}")

        # create random friendships
        # generate list of all possible friendships
        possibleFriendships = []
        # avoid dupes by ensuring first id 
        # is smaller than second
        for userID in self.users:
            for friendID in range(userID + 1, self.last_id + 1):
                possibleFriendships.append((userID, friendID))
        
        print(f"\npossibleFriendships : {possibleFriendships}\n")

        # shuffle list
        random.shuffle(possibleFriendships)
        print(f"\nrandom friendships : {possibleFriendships}\n")


        # slice off total_friendships from front to create friendships
        totalFriendships = avgFriendships * numUsers // 2
        print(f"\nfriendships to create : {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.add_friendship(friendship[0], friendship[1])


      


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(11, 3)
    print("\nUSERS: ")
    print(sg.users)
    print("\nFRIENDSHIPS: ")
    print(sg.friendships)
    print("\n")
    connections = sg.get_all_social_paths(1)
    print(connections)
