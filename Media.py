# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: Media class

class Media:

    # Member variables to store an ID, a title, and an average rating
    _id = ""
    _title = ""
    _avgRating = 0

    # constructor that takes in an ID, a title, and an average rating as parameters and assigns those values to the appropriate member variables
    def __init__(self, id, title, avgRating):
        self._id = id
        self._title = title
        self._avgRating = avgRating

    # accessor/mutator functions
    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def getAvgRating(self):
        return self._avgRating

