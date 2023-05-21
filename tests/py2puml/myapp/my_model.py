class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class BlogPost:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author
