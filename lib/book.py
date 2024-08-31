#!/usr/bin/env python3

class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        '''The title property'''
        return self._title
    
    @title.setter
    def title(self, title):
        print(f"Setting title to {title}")
        self._title = title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):

        if isinstance(page_count, int):
            print(f"Setting page_count to {page_count}")
            self._page_count = page_count 
        else:
            print("page_count must be an integer")

    def turn_page(self):
        '''Outputs a message indicating that the page has been turned.'''
        print("Flipping the page...wow, you read fast!")
        
               

book = Book("And Then There Were None", 272)
book.title = "The good place"
book.page_count = 1322
book.turn_page()
print(book.title, book.page_count)

    
        