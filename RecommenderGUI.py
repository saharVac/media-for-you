# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: RecommenderGUI class

from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
class RecommenderGUI:

    # A constructor function that takes in no parameters
    def __init__(self):
        # Creates an instance of a Recommender object and stores it in a variable
        self.__recommender = Recommender()

        # Creates a Toplevel main window, with an appropriate title, and dimensions of 1200 pixels wide by 800 pixels tall
        self.__main_window = tk.Tk()

        self.__main_window.title("Movie Recommender")
        self.__main_window.geometry("1000x600")

        # notebook tab
        self.__notebook = ttk.Notebook(self.__main_window)
        self.__notebook.pack(expand=1, fill=tk.BOTH)

        # Contains a notebook tab to display all of the movie titles and runtimes, as well as the movie statistics
        self.__movie_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__movie_tab, text="Movies")


        # This tab should be populated using the appropriate functions from the Recommender object
        self.__movie_list = self.__recommender.getMovieList()
        # self.__movie_stats = self.__recommender.getMovieStats()

        self.__movie_text1 = tk.Text(self.__movie_tab, wrap="word")
        self.__movie_text1.pack(expand=1, fill=tk.BOTH)

        if self.__movie_list:
            # Populate the text widget with movie data
            self.__movie_text1.insert("end", self.__movie_list)
        else:
            # Display default text if no data has been loaded yet
            self.__movie_text1.insert("end", "No data has been loaded yet.")

        # text widget for movi statistics
        self.__movie_text2 = tk.Text(self.__movie_tab, wrap="word")
        self.__movie_text2.insert(tk.END, self.__movie_list)
        self.__movie_text2.pack(expand=1, fill=tk.BOTH)

        # The user should be able to scroll through the title and runtimes
        self.__scrollbar = tk.Scrollbar(self.__movie_tab, command=self.__movie_text1.yview)
        self.__scrollbar.pack(side="right", fill="y")
        self.__movie_text1.config(yscrollcommand=self.__scrollbar.set)

        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet


        # The user should not be able to alter the data in the text areas
        self.__movie_text1.configure(state=tk.DISABLED)
        self.__movie_text2.configure(state=tk.DISABLED)



        # Contains a notebook tab to display all of the tv show titles and seasons, as well as the tv show statistics
            # This tab should be populated using the appropriate functions from the Recommender object
            # The user should be able to scroll through the title and seasons
            # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
            # The user should not be able to alter the data in the text areas

        self.__show_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__show_tab, text="TV shows")
        self.__show_text = tk.Text(self.__show_tab, state="disabled")
        self.__show_text.pack()

        # self.__load_tv_shows_button = tk.Button(self.__tv_show_tab, text="Load TV Shows", command=self.__recommender.loadShows)

        # Contains a notebook tab to display all of the book titles and authors, as well as the book statistics
            # This tab should be populated using the appropriate functions from the Recommender object
            # The user should be able to scroll through the title and authors
            # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
            # The user should not be able to alter the data in the text areas

        self.__book_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__book_tab, text="Books")
        self.__book_text = tk.Text(self.__book_tab, state="disabled")
        # self.__load_books_button = tk.Button(self.__book_tab, text="Load Books", command=self.__recommender.loadBooks())

        # Contains a notebook tab to allow the user to search through the movies and tv shows and should contain
            # A Combobox with the options Movie and TV Show
            # Appropriate Label and Entry widgets to collection information regarding the title, director, actor, and/or genre
            # A Button to trigger the search, which calls the appropriate function from the Recommender object and stores the results in the text area
            # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
            # The user should be able to scroll through the results
            # The user should not be able to alter the data in the text area

        self.__search_movies_tvshows = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_movies_tvshows, text="Search Movies/TV")


        # Contains a notebook tab to allow the user to search through the books and should contain
            # Appropriate Label and Entry widgets to collection information regarding the title, author, and/or publisher
            # A Button to trigger the search, which calls the appropriate function from the Recommender object and stores the results in the text area
            # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
            # The user should be able to scroll through the results
            # The user should not be able to alter the data in the text area


        self.__search_books = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_books, text="Search Books")

        # Contains a notebook tab to allow the user to obtain media recommendations and should contain
            # A Combobox with the options Movie, TV Show, Book
            # Appropriate Label and Entry widgets to collection information regarding the title
            # A Button to trigger the recommendation search, which calls the appropriate function from the Recommender object and stores the results in the text area
            # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter a title to receive a recommendation
            # The user should be able to scroll through the results
            # The user should not be able to alter the data in the text area

        self.__recommendation_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__recommendation_tab, text="Recommendation")



        # Buttons below the notebook that will have appropriate names and will:
            # Load the show data using the loadShows()function
            # Load the book data using the loadBooks()function
            # Load the association data using the loadAssociations()
            # Spawn a dialog containing the information regarding your team using the creditInfoBox()
            # Quit the program
        self.__button_frame = ttk.Frame(self.__notebook)

        self.__load_shows_button = tk.Button(self.__button_frame, text="Load Shows", command=self.loadShows)
        self.__load_books_button = tk.Button(self.__button_frame, text="Load Books")
        self.__load_association_button = tk.Button(self.__button_frame, text="Load Associations")
        self.__information_button = tk.Button(self.__button_frame, text="Information")
        self.__quit_button = tk.Button(self.__button_frame, text="Quit", command=self.__main_window.destroy)

        self.__load_shows_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.__load_books_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.__load_association_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.__information_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.__quit_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.__button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # mainloop to run tkinter
        self.__main_window.mainloop()

    # A loadShows() function that takes in no parameters, returns nothing, and:
        # Calls the appropriate function from the Recommender object to read in all of the data for the shows
        # Calls the appropriate function from the Recommender object to obtain the string representing the list of movies and the string representing the movie statistics and displays them in the appropriate text area
        # Calls the appropriate function from the Recommender object to obtain the string representing the list of tv shows and the string representing the tv show statistics and displays them in the appropriate text area
    def loadShows(self):
        show_data = self.__recommender.loadShows()
        movie_list = self.__recommender.getMovieList()
        movie_stats = self.__recommender.getMovieStats()

        if movie_list:
            self.__movie_text1.configure(state=tk.NORMAL)
            self.__movie_text1.delete(1.0, tk.END)
            self.__movie_text1.insert(tk.END, movie_list)
            self.__movie_text1.configure(state=tk.DISABLED)
        else:
            self.__movie_text1.configure(state=tk.NORMAL)
            self.__movie_text1.delete(1.0, tk.END)
            self.__movie_text1.insert(tk.END, "No data available")
            self.__movie_text1.configure(state=tk.DISABLED)

        if movie_stats:
            self.__movie_text2.configure(state=tk.NORMAL)
            self.__movie_text2.delete(1.0, tk.END)
            self.__movie_text2.insert(tk.END, movie_stats)
            self.__movie_text2.configure(state=tk.DISABLED)
        else:
            self.__movie_text2.configure(state=tk.NORMAL)
            self.__movie_text2.delete(1.0, tk.END)
            self.__movie_text2.insert(tk.END, "No statistics available")
            self.__movie_text2.configure(state=tk.DISABLED)




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



###########TESTING###########
new = RecommenderGUI()