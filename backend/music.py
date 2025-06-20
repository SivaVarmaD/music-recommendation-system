class Music:
    def __init__(self, id, name, date, author, language, style):
        self.id = id
        self.name = name
        self.date = date
        self.author = author
        self.language = language
        self.style = style

    def display(self):
        print("id:", self.id)
        print("Name:", self.name)
        print("Date:", self.date)
        print("Author:", self.author)
        print("Language:", self.language)
        print("Style:", self.style)
        print()
