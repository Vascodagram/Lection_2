"""
Задание 1
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
равенство и неравенство, методы __repr__ и __str__.
Задание 2
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class Book:
    def __init__(self, author, name, publication_date, genre, comments='No comments'):
        self.author = author
        self.name = name
        self.publication_data = publication_date
        self.genre = genre
        self.comments = comments

    def __eq__(self, other):
        return self.author == other.author and \
            self.name == other.name and \
            self.publication_data == other.publication_data and \
            self.genre == other.genre

    def __str__(self):
        if self.comments == 'No comments':
            return f"{self.author} by {self.name}. Publisher in {self.publication_data}, genre: {self.genre}"
        else:
            return f"{self.author} by {self.name}. Publisher in {self.publication_data}, genre: {self.genre}\
            \n{'*'*10}\n{self.comments}"

    def __repr__(self):
        return f"{self.author}, {self.name}, {self.publication_data}, {self.genre}"


class Comment:
    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.comment = comment

    def __str__(self):
        return f'User: {self.user}.\nBook: "{self.book}"\nComment: {self.comment}'

    def __repr__(self):
        return f'{self.user, self.comment, self.book}'


# com1 = Comment('Petr', "Ten little negro", "very good")
# com2 = Comment('Igor', "TThe Financier", "nice")
# com3 = Comment("Vladimir", "Don Quixote", "interesting")
com1 = Comment('Petr', "Ten little negro", "very good")
book_1 = Book("Agatha Christie", "Ten little negro", 1939, "Psychological thriller", str(com1))
book_2 = Book("Theodore Dreiser", "The Financier", 1912, "Novel")
print(book_1)
print()
print(book_2 == book_1)


