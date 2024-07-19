from user import User
class Graph:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_friendship(self, user_id1, user_id2):
        self.users[user_id1].add_friend(user_id2)
        self.users[user_id2].add_friend(user_id1)

    def suggest_song_between_users(self, user_id1, user_id2, criteria, value):
        user1 = self.users.get(user_id1)
        user2 = self.users.get(user_id2)
        if user1 and user2:
            if criteria == 'author':
                suggested_song = user1.suggest_song_by_author(user2, value)
            elif criteria == 'language':
                suggested_song = user1.suggest_song_by_language(user2, value)
            elif criteria == 'style':
                suggested_song = user1.suggest_song_by_style(user2, value)
            else:
                print("Invalid suggestion criteria.")
                return

            if suggested_song:
                suggested_song.display()
            else:
                print("No common liked song found between the users.")