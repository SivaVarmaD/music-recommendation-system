from music import Music

class music_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class music_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_object(self, m):
        node = music_node(m)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, id, name, date, author, language, style):
        m = Music(id, name, date, author, language, style)
        node = music_node(m)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def search_id(self, id):
        current = self.head
        while current:
            if current.data.id == id:
                return current.data
            current = current.next
        return None

    def search_name(self, name):
        current = self.head
        while current:
            if current.data.name == name:
                current.data.display()
            current = current.next

    def search_date(self, date):
        current = self.head
        while current:
            if current.data.date == date:
                current.data.display()
            current = current.next

    def search_author(self, author):
        current = self.head
        while current:
            if current.data.author == author:
                current.data.display()
            current = current.next
        return None

    def search_language(self, language):
        current = self.head
        while current:
            if current.data.language == language:
                current.data.display()
            current = current.next
        return None

    def search_style(self, style):
        current = self.head
        while current:
            if current.data.style == style:
                current.data.display()
            current = current.next
        return None

    def display(self):
        current = self.head
        while current:
            current.data.display()
            current = current.next

    def iterate(self):
        current = self.head
        while current:
            yield current
            current = current.next