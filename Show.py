# Author: Samradnyee
# Date created: 4/23/24
# Description: Show class, that is a subclass of Media
from Media import Media

class Show(Media):
    # Member variables to store the type of show, directors, actors, a country code, the date the
    # show was added, the year the show was released, the rating, the duration, genres, and a
    # description
    __type = ""
    __directors = []
    __actors = []
    __country_code = ""
    __add_date = ""
    __release_year = ""
    __rating = 0
    __duration = 0
    __genres = []
    __description = ""

    # constructor that takes in an ID, a title, an average rating, the type of show,
    # directors, actors, a country code, the date the show was added, the year the show was
    # released, the rating, the duration, genres, and a description as parameters and assigns those
    # values to the appropriate member variables
    def __init__(self, id, title, avg_rating, type, directors, actors, country_code, add_date, release_year, rating, duration, genres, description):
        """
        :param id:
        :param title:
        :param avg_rating:
        :param type:
        :param directors:
        :param actors:
        :param country_code:
        :param add_date:
        :param release_year:
        :param rating:
        :param duration:
        :param genres:
        :param description:
        """

        Media.__init__(id, title, avg_rating)

        self.__type = type
        self.__directors = directors
        self.__actors = actors
        self.__country_code = country_code
        self.__add_date = add_date
        self.__release_year = release_year
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    # accessor/mutator functions

    def getType(self):
        return self.__type

    def getDirectors(self):
        return self.__directors

    def getActors(self):
        return self.__actors

    def getCountryCode(self):
        return self.__country_code

    def getAddDate(self):
        return self.__add_date

    def getReleaseYear(self):
        return self.__release_year

    def getRating(self):
        return self.__rating

    def getDuration(self):
        return self.__duration

    def getGenres(self):
        return self.__genres

    def getDescription(self):
        return self.__description
