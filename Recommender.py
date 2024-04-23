# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: Recommender class

# constructor that instantiates three dictionaries
    # one to store Book objects, where the book’s id is the key and the value is the object
    # one to store Show objects, where the show’s id is the key and the value is the object
    # one to store dictionaries keeping track of associations, where a show or book id is the key and the value is a dictionary
        # For the inner dictionary, the key should be a show or book id and the value is the number of times the outer id and inner id are associated

# function named loadBooks(), that takes in no additional parameters, returns nothing, loads all of the data from a book file, and which should at least:
    # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
    # Opens and reads the file one entry at a time
    # Stores the entry for each book in a Book object
    # Stores each Book object in the appropriate dictionary using the book’s ID as the key and the Book object as the value
    # Close the file once all of the data has been read in

# A function named loadShows(), that takes in no additional parameters, returns nothing, loads all of the data from a show file, and which should at least:
    # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
    # Opens and reads the file one entry at a time
    # Stores the entry for each show in a Show object
    # Stores each Show object in the appropriate dictionary using the show’s ID as the key and the Show object as the value
    # Close the file once all of the data has been read in

# A function named loadAssociations(), that takes in no additional parameters, returns nothing, loads all of the data from an association file, and which should at least::
    # Prompts the user for the name of the file using an appropriate filedialog, and if the user does not choose an existing file, it should repeatedly prompt the user for a file in the same way
    # Opens and reads the file one entry at a time
    # Using the first id as a key, determine if there is a dictionary associated with it
        # It not, create a new dictionary and then add the second id to the new dictionary so that the second id is associated with the value 1
        # Otherwise, determine if the second id is a key in the second dictionary
            # If it is, increment the count associated with it by 1
            # Otherwise, set the count associated with it to 1
    # Perform the same steps again, but this time use the second id for the outer dictionary and the first id for the inner dictionary
    # Close the file once all of the data has been read in

# A function named getMovieList(), that takes in no additional parameters, and returns the Title and Runtime for all of the stored movies, such that:
    # The data has the header Title and Movie
    # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data

# A function named getTVList(), that takes in no additional parameters, and returns the Title and Number of Seasons for all of the stored tv shows, such that:
    # The data has the header Title and Seasions
    # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data

# A function named getBookList(), that takes in no additional parameters, and returns the Title and Author(s) for all of the stored movies, such that:
    # The data has the header Title and Author(s)
    # All of the data is in neat, even columns, whose width is determined based on the length of the entries in the data

# A function named getMovieStats(), that takes in no additional parameters, and returns the statistics regarding movies, such as:
    # Rating for movies (G, PG, R, etc...) and the number of times a particular rating appears as a percentage of all of the ratings for movies, with two decimals of precision
    # Average movie duration in minutes, with two decimals of precision
    # The director who has directed the most movies
    # The actor who has acted in the most movies
    # The most frequent movie genre

# A function named getTVStats(), that takes in no additional parameters, and returns the statistics regarding tv shows, such as:
    # Rating for tv shows (G, PG, R, etc...) and the number of times a particular rating appears as a percentage of all of the ratings for tv shows, with two decimals of precision
    # Average number of seasons for tv shows, with two decimals of precision The actor who has acted in the most tv shows
    # The most frequent tv show genre

# A function named getBookStats(), that takes in no additional parameters, and returns the statistics regarding books, such as:
    # The average page count, with two decimals of precision
    # The author who has written the most books
    # The publisher who has published the most books

# A function named searchTVMovies(), that takes in strings representing a movie or tv show, a title, a director, an actor, and a genre, and returns information regarding Movies or TV Shows such that:
    # If the string representing the movie or tv show is neither Movie nor TV Show, spawn a showerror messagebox and inform the user the need to select Movie or TV Show from Type first, and return the string No Results
    # If the strings representing title, director, actor, and genre are all empty, spawn a showerror messagebox and inform the user the need to enter information for the Title, Directory, Actor and/or Genre first, and return the string No Results
    # Otherwise, search through the dictionary of shows and select all objects that adhere to the user’s data
    # Return a string containing the Title, Director, Actors, and Genre (with those titles at the top) in neat, even columns, whose width is determined based on the length of the entries in the data

# A function named searchBooks(), that takes in strings representing a title, an author, and a publisher, and returns information regarding books such that:
    # If the strings representing title, author, and publisher are all empty, spawn a showerror messagebox and inform the user the need to enter information for the Title, Author, and/or Publisher first, and return the string No Results
    # Otherwise, search through the dictionary of books and select all objects that adhere to the user’s data
    # Return a string containing the Title, Author, and Publisher (with those titles at the top) in neat, even columns, whose width is determined based on the length of the entries in the data

# A function named getRecommendations(), that takes in strings representing a type and a title, and returns a string containing recommendations regarding Movies, TV Shows, or Books such that:
    # If the type is Movie or TV Show, search through the shows dictionary and determine the id associated with that title
        # If the title is not in the dictionary, spawn a showwarning messagebox informing the user that there are no recommendations for that title, and return No results
        # Otherwise, using that movie or tv show id, determine all of the books associated with that id in the association dictionary, and return a string containing all of the information for each book with appropriate titles for each piece of information
    # If the type is Book, search through the books dictionary and determine the id associated with that title
        # If the title is not in the dictionary, spawn a showwarning messagebox informing the user that there are no recommendations for that title, and return No results
        # Otherwise, using that book id, determine all of the movies and tv shows associated with that id in the association dictionary, and return a string containing all of the information for each movie or tv show with appropriate titles for each piece of information
