from musiclist import music_list
from music import Music
from user import User
from graph import Graph

def display_menu():
    print("************ Menu ************")
    print("a. Display Music List")
    print("b. Add New Music")
    print("c. Add New User")
    print("d. Create Friendship")
    print("e. Add Liked Music to User")
    print("f. Suggest Song Between Users")
    print("g. Display Friends of User")
    print("x. Exit")
    print("******************************")

def main():
    musiclist = music_list()
    musiclist.insert(1, "Song 1", "2024-01-01", "Author Name", "English", "Pop")
    musiclist.insert(2, "Song 2", "2024-02-01", "Another Author", "Spanish", "Rock")
    musiclist.insert(3, "Song 3", "2024-03-01", "Author Name", "English", "Jazz")
    musiclist.insert(4, "Song 4", "2024-04-01", "Yet Another Author", "French", "Classical")
    musiclist.insert(5, "Song 5", "2024-05-01", "New Artist", "German", "Electronic")
    musiclist.insert(6, "Song 6", "2024-06-01", "Famous Singer", "English", "Pop")
    musiclist.insert(7, "Song 7", "2024-07-01", "Old Singer", "French", "Blues")
    musiclist.insert(8, "Song 8", "2024-08-01", "Cool Band", "Spanish", "Funk")
    musiclist.insert(9, "Song 9", "2024-09-01", "Indie Artist", "English", "Indie")
    musiclist.insert(10, "Song 10", "2024-10-01", "Band Name", "Portuguese", "Samba")
    musiclist.insert(11, "Song 11", "2024-11-01", "Solo Artist", "Japanese", "Pop")
    musiclist.insert(12, "Song 12", "2024-12-01", "Duo Band", "Korean", "R&B")

    graph = Graph()

    id = 13
    userid = 3

    while True:
        display_menu()
        user_input = input("Enter your choice: ")

        if user_input == "a":
            print("\n--- Music List ---")
            musiclist.display()
            print("------------------\n")

        elif user_input == "b":
            print("\n--- Add New Music ---")
            name = input("Enter name: ")
            date = input("Enter date: ")
            author = input("Enter author: ")
            language = input("Enter language: ")
            style = input("Enter style: ")
            print("Music is added with ID:", id)
            musiclist.insert(id, name, date, author, language, style)
            id += 1
            print("---------------------\n")

        elif user_input == "c":
            print("\n--- Add New User ---")
            print("Your user ID is", userid)
            graph.add_user(userid)
            userid += 1
            print("---------------------\n")

        elif user_input == "d":
            print("\n--- Create Friendship ---")
            user1 = int(input("Enter user id 1: "))
            user2 = int(input("Enter user id 2: "))
            graph.add_friendship(user1, user2)
            print("Friendship is created between", user1, "and", user2)
            print("------------------------\n")

        elif user_input == "e":
            print("\n--- Add Liked Music to User ---")
            user = int(input("Enter user id: "))
            user_object = graph.users.get(user)
            if user_object:
                print("\n--- Music List ---")
                musiclist.display()
                print("------------------")
                music_id = int(input("Enter music ID: "))
                music = musiclist.search_id(music_id)
                if music:
                    user_object.music_liked.insert_object(music)
                    print("Music added to user's liked list.")
                else:
                    print("Invalid music ID.")
            else:
                print("User not found.")
            print("-----------------------------\n")

        elif user_input == "f":
            print("\n--- Suggest Song Between Users ---")
            user1 = int(input("Enter user id 1: "))
            user2 = int(input("Enter user id 2: "))
            criteria = input("Enter criteria (author/language/style): ")
            value = input("Enter value: ")
            graph.suggest_song_between_users(user1, user2, criteria, value)
            print("-----------------------------------\n")

        elif user_input == "g":
            print("\n--- Display Friends of User ---")
            user = int(input("Enter user id : "))
            graph.users[user].display_friends()
            print("--------------------------------\n")

        elif user_input == "x":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()
