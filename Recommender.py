# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: Recommender class
import os
from tkinter import filedialog
from tkinter import messagebox
from Book import Book
from Show import Show

class Recommender:

    # constructor that instantiates three dictionaries
    def __init__(self):
        # one to store Book objects, where the book’s id is the key and the value is the object
        self._books = {}
        # one to store Show objects, where the show’s id is the key and the value is the object
        self._shows = {}
        # one to store dictionaries keeping track of associations, where a show or book id is the key and the value is
        # a dictionary
        # For the inner dictionary, the key should be a show or book id and the value is the number of times the outer
        # id and inner id are associated
        self._associations = {}

    # function named loadBooks(), that takes in no additional parameters, returns nothing, loads all of the data from a book file, and which should at least:
    def loadBooks(self):
        # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
        booksFile = filedialog.askopenfilename(title="Provide with books file name", initialdir=os.getcwd())
        while True:
            if os.path.exists(booksFile):
                break
            else:
                booksFile = filedialog.askopenfilename(title="File does not exist, please provide with books file name", initialdir=os.getcwd())
        # Opens and reads the file one entry at a time
        with open(booksFile, "r") as file:
            lines = file.readlines()
            # iterating over lines, skipping header row
            for line in lines[1:]:
                line = line.strip()
                lineList = line.split(",")
                bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, publication_date, publisher = lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7], lineList[8], lineList[9], lineList[10]
                # Stores the entry for each book in a Book object

                book = Book(bookID, title, average_rating, authors, isbn, isbn13, language_code, num_pages, ratings_count, publication_date, publisher)
                # Stores each Book object in the appropriate dictionary using the book’s ID as the key and the Book object as the value
                self._books[bookID] = book
        # Close the file once all of the data has been read in

    # A function named loadShows(), that takes in no additional parameters, returns nothing, loads all of the data from a show file, and which should at least:
    def loadShows(self):
        # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
        showsFile = filedialog.askopenfilename(title="Provide with shows file name", initialdir=os.getcwd())
        while True:
            if os.path.exists(showsFile):
                break
            else:
                showsFile = filedialog.askopenfilename(title="File does not exist, please provide with shows file name", initialdir=os.getcwd())
        # Opens and reads the file one entry at a time
        with open(showsFile, "r") as file:
            lines = file.readlines()
            # iterating over lines, skipping header row
            for line in lines[1:]:
                line = line.strip()
                lineList = line.split(",")
                show_id, type, title, director, cast, average_rating, country, date_added, release_year, rating, duration, listed_in, description = lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7], lineList[8], lineList[9], lineList[10], lineList[11], lineList[12]
                # Stores the entry for each show in a Show object
                show = Show(show_id, title, average_rating, type, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
                # Stores each Show object in the appropriate dictionary using the show’s ID as the key and the Show object as the value
                self._shows[show_id] = show
        # Close the file once all of the data has been read in

    # A function named loadAssociations(), that takes in no additional parameters, returns nothing, loads all of the data from an association file:
    def loadAssociations(self):
        # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
        associationFile = filedialog.askopenfilename(title="Provide with association file name", initialdir=os.getcwd())
        while True:
            if os.path.exists(associationFile):
                break
            else:
                associationFile = filedialog.askopenfilename(title="File does not exist, please provide with association file name", initialdir=os.getcwd())
        # Opens and reads the file one entry at a time
        with open(associationFile, "r") as file:
            lines = file.readlines()
            # iterating over lines
            for line in lines:
                line = line.strip()
                lineList = line.split(",")
                # Using the first id as a key, determine if there is a dictionary associated with it
                isDictAssoc = lineList[0] in self._associations
                if not isDictAssoc:
                    # If not, create a new dictionary and then add the second id to the new dictionary so that the second id is associated with the value 1
                    self._associations[lineList[0]] = {}
                    self._associations[lineList[0]][lineList[1]] = 1
                else:
                    # Otherwise, determine if the second id is a key in the second dictionary
                    if lineList[1] in self._associations[lineList[0]]:
                        # If it is, increment the count associated with it by 1
                        self._associations[lineList[0]][lineList[1]] += 1
                    else:
                        # Otherwise, set the count associated with it to 1
                        self._associations[lineList[0]][lineList[1]] = 1
                # Perform the same steps again, but this time use the second id for the outer dictionary and the first id for the inner dictionary
                isDictAssoc = lineList[1] in self._associations
                if not isDictAssoc:
                    # If not, create a new dictionary and then add the second id to the new dictionary so that the second id is associated with the value 1
                    self._associations[lineList[1]] = {}
                    self._associations[lineList[1]][lineList[0]] = 1
                else:
                    # Otherwise, determine if the second id is a key in the second dictionary
                    if lineList[0] in self._associations[lineList[1]]:
                        # If it is, increment the count associated with it by 1
                        self._associations[lineList[1]][lineList[0]] += 1
                    else:
                        # Otherwise, set the count associated with it to 1
                        self._associations[lineList[1]][lineList[0]] = 1
        # Close the file once all of the data has been read in

    # A function named getMovieList(), that takes in no additional parameters, and returns the Title and Runtime for all of the stored movies, such that:
    def getMovieList(self):
        titles = []
        maxTitleLength = 0
        durations = []
        for id, show in self._shows.items():
            if show.getType() == "Movie":
                title = show.getTitle()
                duration = show.getDuration()
                titles.append(title)
                durations.append(duration)
                if len(title) > maxTitleLength:
                    maxTitleLength = len(title)
        # The data has the header Title and Movie
        data = f"{'Title':<{maxTitleLength}}  Runtime"
        for index, title in enumerate(titles):
            # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data
            data += f"\n{title:<{maxTitleLength}}  {durations[index]}"
        return data

    # A function named getTVList(), that takes in no additional parameters, and returns the Title and Number of Seasons for all of the stored tv shows, such that:
    def getTVList(self):
        titles = []
        maxTitleLength = 0
        durations = []
        for id, show in self._shows.items():
            if show.getType() == "TV Show":
                title = show.getTitle()
                duration = show.getDuration()
                titles.append(title)
                durations.append(duration)
                if len(title) > maxTitleLength:
                    maxTitleLength = len(title)
        # The data has the header Title and Seasons
        data = f"{'Title':<{maxTitleLength}}  Seasons"
        for index, title in enumerate(titles):
            # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data
            data += f"\n{title:<{maxTitleLength}}  {durations[index]}"
        return data

    # A function named getBookList(), that takes in no additional parameters, and returns the Title and Author(s) for all of the stored movies, such that:
    def getBookList(self):
        titles = []
        maxTitleLength = 0
        authors = []
        for id, book in self._books.items():
            title = book.getTitle()
            author = book.getAuthors()
            titles.append(title)
            authors.append(author)
            if len(title) > maxTitleLength:
                maxTitleLength = len(title)
        # The data has the header Title and Author(s)
        data = f"{'Title':<{maxTitleLength}}  Author(s)"
        for index, title in enumerate(titles):
            # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data
            data += f"\n{title:<{maxTitleLength}}  {authors[index]}"
        return data


    # A function named getMovieStats(), that takes in no additional parameters, and returns the statistics regarding movies, such as:
    def getMovieStats(self):
        totalDurations = 0
        totalMovies = 0

        ratingToMovieAmounts = {}

        directorsToMovieAmounts = {}
        directorWithMostMovies = ""

        actorsToMovieAmounts = {}
        actorInMostMovies = ""

        genreCounts = {}
        genreWithMostMovies = ""

        for id, show in self._shows.items():
            if show.getType() == "Movie":

                # incrementing duration total toward average to calculate once iteration done
                duration = int(show.getDuration().split(" ")[0])
                totalDurations += duration
                totalMovies += 1

                directors = show.getDirectors().split("\\")
                for director in directors:
                    if director:
                        if director not in directorsToMovieAmounts:
                            # if directorsToMovieAmounts is empty, this first director found should be declared as one with most movies for now
                            if not directorsToMovieAmounts:
                                directorWithMostMovies = director
                            directorsToMovieAmounts[director] = 1
                        else:
                            directorsToMovieAmounts[director] += 1
                            # check if director now has highest amount
                            if directorsToMovieAmounts[director] > directorsToMovieAmounts[directorWithMostMovies]:
                                directorWithMostMovies = director

                actors = show.getActors().split("\\")
                for actor in actors:
                    if actor:
                        if actor not in actorsToMovieAmounts:
                            # if actorsToMovieAmounts is empty, this first actor found should be declared as one with most movies for now
                            if not actorsToMovieAmounts:
                                actorInMostMovies = actor
                            actorsToMovieAmounts[actor] = 1
                        else:
                            actorsToMovieAmounts[actor] += 1
                            if actorsToMovieAmounts[actor] > actorsToMovieAmounts[actorInMostMovies]:
                                actorInMostMovies = actor

                genres = show.getGenres().split("\\")
                for genre in genres:
                    if genre not in genreCounts:
                        # if genreCounts is empty, this first genre found should be declared as one in most movies for now
                        if not genreCounts:
                            genreWithMostMovies = genre
                        genreCounts[genre] = 1
                    else:
                        genreCounts[genre] += 1
                        # check if genre now has highest amount
                        if genreCounts[genre] > genreCounts[genreWithMostMovies]:
                            genreWithMostMovies = genre

                rating = show.getRating()
                if rating:
                    if rating not in ratingToMovieAmounts:
                        ratingToMovieAmounts[rating] = 1
                    else:
                        ratingToMovieAmounts[rating] += 1

        # Rating for movies (G, PG, R, etc...) and the number of times a particular rating appears as a percentage of all of the ratings for movies, with two decimals of precision
        stats = "Ratings:"
        ratingPercentages = {}
        for rating, amount in ratingToMovieAmounts.items():
            ratingPercentages[rating] = f"{(amount / totalMovies):.2f}"
            stats += f"\n{rating} {(amount / totalMovies):.2%}"

        # Average movie duration in minutes, with two decimals of precision
        avgDuration = totalDurations / totalMovies
        stats += f"\n\nAverage Movie Duration: {avgDuration:.2f} minutes"

        # The director who has directed the most movies
        stats += f"\n\nMpst Prolific Director: {directorWithMostMovies}"

        # The actor who has acted in the most movies
        stats += f"\n\nMost Prolific Actor: {actorInMostMovies}"

        # The most frequent movie genre
        stats += f"\n\nMost Frequent Genre: {genreWithMostMovies}"

        return stats, ratingPercentages

    # A function named getTVStats(), that takes in no additional parameters, and returns the statistics regarding tv shows, such as:
    def getTVStats(self):
        totalSeasons = 0
        totalShows = 0

        ratingToShowAmounts = {}

        actorsToShowAmounts = {}
        actorInMostShows = ""

        genreCounts = {}
        genreWithMostShows = ""

        for id, show in self._shows.items():
            if show.getType() == "TV Show":

                seasons = int(show.getDuration().split(" ")[0])
                totalSeasons += seasons
                totalShows += 1

                actors = show.getActors().split("\\")
                for actor in actors:
                    if actor:
                        if actor not in actorsToShowAmounts:
                            # if actorsToShowAmounts is empty, this first actor found should be declared as one with most shows for now
                            if not actorsToShowAmounts:
                                actorInMostShows = actor
                            actorsToShowAmounts[actor] = 1
                        else:
                            actorsToShowAmounts[actor] += 1
                            if actorsToShowAmounts[actor] > actorsToShowAmounts[actorInMostShows]:
                                actorInMostShows = actor

                genres = show.getGenres().split("\\")
                for genre in genres:
                    if genre not in genreCounts:
                        # if genreCounts is empty, this first genre found should be declared as one in most shows for now
                        if not genreCounts:
                            genreWithMostShows = genre
                        genreCounts[genre] = 1
                    else:
                        genreCounts[genre] += 1
                        # check if genre now has highest amount
                        if genreCounts[genre] > genreCounts[genreWithMostShows]:
                            genreWithMostShows = genre

                rating = show.getRating()
                # accounting for null value verification
                if rating:
                    if rating not in ratingToShowAmounts:
                        ratingToShowAmounts[rating] = 1
                    else:
                        ratingToShowAmounts[rating] += 1

        # Rating for tv shows (G, PG, R, etc...) and the number of times a particular rating appears as a percentage of all of the ratings for tv shows, with two decimals of precision
        ratingPercentages = {}
        stats = "Ratings:"
        for rating, amount in ratingToShowAmounts.items():
            ratingPercentages[rating] = f"{(amount / totalShows):.2f}"
            stats += f"\n{rating} {amount / totalShows:.2%}"

        # Average number of seasons for tv shows, with two decimals of precision
        avgSeasons = totalSeasons / totalShows
        stats += f"\n\nAverage Number of Seasons: {avgSeasons:.2f} seasons"

        # The actor who has acted in the most tv shows
        stats += f"\n\nMost Prolific Actor: {actorInMostShows}"

        # The most frequent tv show genre
        stats += f"\n\nMost Frequent Genre: {genreWithMostShows}"

        return stats, ratingPercentages

    # A function named getBookStats(), that takes in no additional parameters, and returns the statistics regarding books, such as:
    def getBookStats(self):
        totalPages = 0

        authorToBookAmounts = {}
        authorInMostBooks = ""

        publisherToBookAmounts = {}
        publisherInMostBooks = ""

        for id, book in self._books.items():
            totalPages += int(book.getPages())

            publisher = book.getPublisher()
            if publisher not in publisherToBookAmounts:
                # if publisherToBookAmounts is empty, this first publisher found should be declared as one in most books for now
                if not publisherToBookAmounts:
                    publisherInMostBooks = publisher
                publisherToBookAmounts[publisher] = 1
            else:
                publisherToBookAmounts[publisher] += 1
                if publisherToBookAmounts[publisher] > publisherToBookAmounts[publisherInMostBooks]:
                    publisherInMostBooks = publisher

            authors = book.getAuthors().split("\\")
            for author in authors:
                if author not in authorToBookAmounts:
                    # if authorToBookAmounts is empty, this first author found should be declared as one in most books for now
                    if not authorToBookAmounts:
                        authorInMostBooks = author
                    authorToBookAmounts[author] = 1
                else:
                    authorToBookAmounts[author] += 1
                    if authorToBookAmounts[author] > authorToBookAmounts[authorInMostBooks]:
                        authorInMostBooks = author

        # The average page count, with two decimals of precision
        avgPages = totalPages / len(self._books)
        stats = f"Average Page Count: {avgPages:.2f} pages"

        # The author who has written the most books
        stats += f"\n\nMost Prolific Author: {authorInMostBooks}"

        # The publisher who has published the most books
        stats += f"\n\nMost Prolific Publisher: {publisherInMostBooks}"

        return stats

    # A function named searchTVMovies(), that takes in strings representing a movie or tv show, a title, a director, an actor, and a genre, and returns information regarding Movies or TV Shows such that:
    def searchTVMovies(self, type, title, director, actor, genre):
        # If the string representing the movie or tv show is neither Movie nor TV Show, spawn a showerror messagebox and inform the user the need to select Movie or TV Show from Type first, and return the string No Results
        if type not in ["Movie", "TV Show"]:
            messagebox.showerror("Error", "Please select Movie or TV Show from Type first")
            return "No Results"
        # If the strings representing title, director, actor, and genre are all empty, spawn a showerror messagebox and inform the user the need to enter information for the Title, Directory, Actor and/or Genre first, and return the string No Results
        elif not title and not director and not actor and not genre:
            messagebox.showerror("Error", "Please enter information for the Title, Directory, Actor and/or Genre first")
            return "No Results"

        # Otherwise, search through the dictionary of shows and select all objects that adhere to the user’s data
        results = []

        longestTitleLen = 0
        longestDirectorLen = 0
        longestActorLen = 0
        longestGenreLen = 0

        for id, show in self._shows.items():
            # since type must be selected, considering only matching types
            if type == show.getType():
                # field by field, considering only non-empty fields, skipping shows that don't match the non-empty fields
                if (title and title != show.getTitle()) or (director and director not in show.getDirectors().split("\\")) or (actor and actor not in show.getActors().split("\\")) or (genre and genre not in show.getGenres().split("\\")):
                    continue
                if len(show.getTitle()) > longestTitleLen:
                    longestTitleLen = len(show.getTitle())
                if len(show.getDirectors()) > longestDirectorLen:
                    longestDirectorLen = len(show.getDirectors())
                if len(show.getActors()) > longestActorLen:
                    longestActorLen = len(show.getActors())
                if len(show.getGenres()) > longestGenreLen:
                    longestGenreLen = len(show.getGenres())
                results.append(show)

        titleColWidth = longestTitleLen if longestTitleLen > len('Title') else len('Title')
        directorColWidth = longestDirectorLen if longestDirectorLen > len('Director') else len('Director')
        actorColWidth = longestActorLen if longestActorLen > len('Actor') else len('Actor')
        genreColWidth = longestGenreLen if longestGenreLen > len('Genre') else len('Genre')

        # Return a string containing the Title, Director, Actors, and Genre (with those titles at the top) in neat, even columns, whose width is determined based on the length of the entries in the data
        data = f"{'Title':<{titleColWidth}}  {'Director':<{directorColWidth}}  {'Actor':<{actorColWidth}}  {'Genre':<{genreColWidth}}"
        for show in results:
            data += f"\n{show.getTitle():<{titleColWidth}}  {show.getDirectors():<{directorColWidth}}  {show.getActors():<{actorColWidth}}  {show.getGenres():<{genreColWidth}}"

        return data

    # A function named searchBooks(), that takes in strings representing a title, an author, and a publisher, and returns information regarding books such that:
    def searchBooks(self, title, author, publisher):
        # If the strings representing title, author, and publisher are all empty, spawn a showerror messagebox and inform the user the need to enter information for the Title, Author, and/or Publisher first, and return the string No Results
        if not title and not author and not publisher:
            messagebox.showerror("Error", "Please enter information for the Title, Author, and/or Publisher first")
            return "No Results"
        # Otherwise, search through the dictionary of books and select all objects that adhere to the user’s data
        results = []

        longestTitleLen = 0
        longestAuthorLen = 0
        longestPublisherLen = 0

        for id, book in self._books.items():
            # field by field, considering only non-empty fields, skipping books that don't match the non-empty fields
            if (title and title != book.getTitle()) or (author and author not in book.getAuthors().split("\\")) or (publisher and publisher != book.getPublisher()):
                continue

            if len(book.getTitle()) > longestTitleLen:
                longestTitleLen = len(book.getTitle())
            if len(book.getAuthors()) > longestAuthorLen:
                longestAuthorLen = len(book.getAuthors())
            if len(book.getPublisher()) > longestPublisherLen:
                longestPublisherLen = len(book.getPublisher())

            results.append(book)

        titleColWidth = longestTitleLen if longestTitleLen > len('Title') else len('Title')
        authorColWidth = longestAuthorLen if longestAuthorLen > len('Author') else len('Author')
        publisherColWidth = longestPublisherLen if longestPublisherLen > len('Publisher') else len('Publisher')

        # Return a string containing the Title, Author, and Publisher (with those titles at the top) in neat, even columns, whose width is determined based on the length of the entries in the data
        data = f"{'Title':<{titleColWidth}}  {'Author':<{authorColWidth}}  {'Publisher':<{publisherColWidth}}"
        for book in results:
            data += f"\n{book.getTitle():<{titleColWidth}}  {book.getAuthors():<{authorColWidth}}  {book.getPublisher():<{publisherColWidth}}"

        return data

    # A function named getRecommendations(), that takes in strings representing a type and a title, and returns a string containing recommendations regarding Movies, TV Shows, or Books such that:
    def getRecommendations(self, type, title):
        # If the type is Movie or TV Show, search through the shows dictionary and determine the id associated with that title
        if type in ["Movie", "TV Show"]:
            idFound = ""
            for id, show in self._shows.items():
                if show.getTitle() == title:
                    idFound = id
            # If the title is not in the dictionary, spawn a showwarning messagebox informing the user that there are no recommendations for that title, and return No results
            if idFound == "":
                messagebox.showwarning("Warning", f"there are no recommendations for title {title}")
                return "No results"
            # Otherwise, using that movie or tv show id, determine all of the books associated with that id in the association dictionary, and return a string containing all of the information for each book with appropriate titles for each piece of information
            else:
                results = ""
                for key in self._associations[idFound].keys():
                    book = self._books[key]
                    results += f"""\rTitle: {book.getTitle()}
                    \rAuthor: {book.getAuthors()}
                    \rAverage Rating: {book.getAvgRating()}
                    \rISBN: {book.getIsbnNum()}
                    \rISBN13: {book.getIsbn13Num()}
                    \rLanguage Code: {book.getLangCode()}
                    \rPages: {book.getPages()}
                    \rRating Count: {book.getRatings()}
                    \rPublication Date: {book.getPublicationDate()}
                    \rPublisher: {book.getPublisher()}
                    
                    \r**************************************************
                    
                    """
                return results
        # If the type is Book, search through the books dictionary and determine the id associated with that title
        elif type == "Book":
            idFound = ""
            for id, book in self._books.items():
                if book.getTitle() == title:
                    idFound = id
            # If the title is not in the dictionary, spawn a showwarning messagebox informing the user that there are no recommendations for that title, and return No results
            if idFound == "":
                messagebox.showwarning("Warning", f"there are no recommendations for title {title}")
                return "No results"
            # Otherwise, using that book id, determine all of the movies and tv shows associated with that id in the association dictionary, and return a string containing all of the information for each movie or tv show with appropriate titles for each piece of information
            else:
                results = ""
                for key in self._associations[idFound].keys():
                    show = self._shows[key]
                    results += f"""\rTitle: {show.getTitle()}
                    \rAverage Rating: {show.getAvgRating()}
                    \rShow Type: {show.getType()}
                    \rDirectors: {show.getDirectors()}
                    \rActors: {show.getActors()}
                    \rCountry Code: {show.getCountryCode()}
                    \rDate Added: {show.getAddDate()}
                    \rRelease Year: {show.getReleaseYear()}
                    \rRating: {show.getRating()}
                    \rDuration: {show.getDuration()}
                    \rGenres: {show.getGenres()}
                    \rDescription: {show.getDescription()}

                    \r**************************************************

                    """
                return results
