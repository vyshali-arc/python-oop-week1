class Library:
   class Book:
     def __init__(self,title,author): 
        self.title=title
        self.author=author
     def display(self):
        print("Book Details:")
        print("Title: ",self.title)
        print("Author: ",self.author)
   def create_book(self):
      book=Library.Book("One Piece","Oda")
      book.display()
lib=Library()
lib.create_book()
          
       