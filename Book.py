# Author: Sahar
# Date created: 4/23/24
# Description: Book class, that is a subclass of Media
from Media import Media

class Book(Media):
    # Member variables to store authors, an isbn number, an isbn13 number, a language code, the
    # number of pages in the book, the number of ratings given to the book, the publication date,
    # and the publisher
    _authors = []
    _isbn_num = 0
    _isbn13_num = 0
    _lang_code = ""
    _pages = 0
    _ratings = 0
    _publication_date = ""
    _publisher = ""

    # constructor that takes in an ID, a title, an average rating, authors, an isbn
    # number, an isbn13 number, a language code, the number of pages in the book, the number of
    # ratings given to the book, the publication date, and the publisher as parameters and assigns
    # those values to the appropriate member variables
    def __init__(self, id, title, avg_rating, authors, isbn_num, isbn13_num, lang_code, pages, ratings, publication_date, publisher):
        """
        :param id:
        :param title:
        :param avg_rating:
        :param authors:
        :param isbn_num:
        :param isbn13_num:
        :param lang_code:
        :param pages:
        :param ratings:
        :param publication_date:
        :param publisher:
        """

        Media.__init__(self, id, title, avg_rating)

        self._authors = authors
        self._isbn_num = isbn_num
        self._isbn13_num = isbn13_num
        self._lang_code = lang_code
        self._pages = pages
        self._ratings = ratings
        self._publication_date = publication_date
        self._publisher = publisher

    # accessor/mutator functions

    def getAuthors(self):
        return self._authors

    def getIsbnNum(self):
        return self._isbn_num

    def getIsbn13Num(self):
        return self._isbn13_num

    def getLangCode(self):
        return self._lang_code

    def getPages(self):
        return self._pages

    def getRatings(self):
        return self._ratings

    def getPublicationDate(self):
        return self._publication_date

    def getPublisher(self):
        return self._publisher
