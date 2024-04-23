# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: RecommenderGUI class

# A constructor function that takes in no parameters and:
    # Creates an instance of a Recommender object and stores it in a variable
    # Creates a Toplevel main window, with an appropriate title, and dimensions of 1200 pixels wide by 800 pixels tall
    # Contains a notebook tab to display all of the movie titles and runtimes, as well as the movie statistics
        # This tab should be populated using the appropriate functions from the Recommender object
        # The user should be able to scroll through the title and runtimes
        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        # The user should not be able to alter the data in the text areas
    # Contains a notebook tab to display all of the tv show titles and seasons, as well as the tv show statistics
        # This tab should be populated using the appropriate functions from the Recommender object
        # The user should be able to scroll through the title and seasons
        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        # The user should not be able to alter the data in the text areas
    # Contains a notebook tab to display all of the book titles and authors, as well as the book statistics
        # This tab should be populated using the appropriate functions from the Recommender object
        # The user should be able to scroll through the title and authors
        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        # The user should not be able to alter the data in the text areas
    # Contains a notebook tab to allow the user to search through the movies and tv shows and should contain
        # A Combobox with the options Movie and TV Show
        # Appropriate Label and Entry widgets to collection information regarding the title, director, actor, and/or genre
        # A Button to trigger the search, which calls the appropriate function from the Recommender object and stores the results in the text area
        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
        # The user should be able to scroll through the results
        # The user should not be able to alter the data in the text area
    # Contains a notebook tab to allow the user to search through the books and should contain
        # Appropriate Label and Entry widgets to collection information regarding the title, author, and/or publisher
        # A Button to trigger the search, which calls the appropriate function from the Recommender object and stores the results in the text area
        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
        # The user should be able to scroll through the results
        # The user should not be able to alter the data in the text area
    # Contains a notebook tab to allow the user to obtain media recommendations and should contain
        # A Combobox with the options Movie, TV Show, Book
        # Appropriate Label and Entry widgets to collection information regarding the title
        # A Button to trigger the recommendation search, which calls the appropriate function from the Recommender object and stores the results in the text area
        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter a title to receive a recommendation
        # The user should be able to scroll through the results
        # The user should not be able to alter the data in the text area
    # Buttons below the notebook that will have appropriate names and will:
        # Load the show data using the loadShows()function
        # Load the book data using the loadBooks()function
        # Load the association data using the loadAssociations()
        # Spawn a dialog containing the information regarding your team using the creditInfoBox()
        # Quit the program

# A loadShows() function that takes in no parameters, returns nothing, and:
    # Calls the appropriate function from the Recommender object to read in all of the data for the shows
    # Calls the appropriate function from the Recommender object to obtain the string representing the list of movies and the string representing the movie statistics and displays them in the appropriate text area
    # Calls the appropriate function from the Recommender object to obtain the string representing the list of tv shows and the string representing the tv show statistics and displays them in the appropriate text area

# A loadBooks() function that takes in no parameters, returns nothing, and:
    # Calls the appropriate function from the Recommender object to read in all of the data for the books
    # Calls the appropriate function from the Recommender object to obtain the string representing the list of books and the string representing the book statistics and displays them in the appropriate text area

# A loadAssociations() function that takes in no parameters, returns nothing, and:
    # Calls the appropriate function from the Recommender object to read in all of the data for the associations

# A creditInfoBox() function that takes in no parameters, returns nothing, and:
    # Spawns a showinfo messagebox containing the names of each of your group members and what day the project was completed on

# A searchShows() function that takes in no parameters, returns nothing, and:
    # Extracts all of the data from the appropriate Combobox and Entry widgets to search for a movie or tv show
    # Calls the appropriate function from the Recommender object to search for a movie or tv show, passing in the information from the Combobox and Entry widgets, and then displaying the returned string in the appropriate text area

# A searchBooks() function that takes in no parameters, returns nothing, and:
    # Extracts all of the data from the appropriate Entry widgets to search for a book
    # Calls the appropriate function from the Recommender object to search for a book, passing in the information from the Entry widgets, and then displaying the returned string in the appropriate text area

# A getRecommendations() function that takes in no parameters, returns nothing, and:
    # Extracts all of the data from the appropriate Combobox and Entry widgets,
    # Calls the appropriate function from the Recommender object to obtain recommendations, passing in the information from the Combobox and Entry widgets, and then displaying the returned string in the appropriate text area
