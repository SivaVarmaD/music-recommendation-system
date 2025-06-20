from musiclist import music_list

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.friends = set()
        self.music_liked = music_list()

    def add_friend(self, friend_id):
        self.friends.add(friend_id)

    def display_friends(self):
        print(f"Friends of user {self.user_id}: {', '.join(str(friend) for friend in self.friends)}")

    def suggest_song_by_author(self, other_user, author):
        common_music = [node.data for node in other_user.music_liked.iterate() if node.data.author == author]
        if common_music:
            return common_music[0]
        else:
            return None

    def suggest_song_by_language(self, other_user, language):
        common_music = [node.data for node in other_user.music_liked.iterate() if node.data.language == language]
        if common_music:
            return common_music[0]
        else:
            return None

    def suggest_song_by_style(self, other_user, style):
        common_music = [node.data for node in other_user.music_liked.iterate() if node.data.style == style]
        if common_music:
            return common_music[0]
        else:
            return None