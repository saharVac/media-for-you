# Author: Sahar and Samradnyee
# Date created: 4/23/24
# Description: RecommenderGUI class

from Recommender import Recommender
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import math

class RecommenderGUI:

    # A constructor function that takes in no parameters
    def __init__(self):
        # Creates an instance of a Recommender object and stores it in a variable
        self.__recommender = Recommender()

        # Creates a Toplevel main window, with an appropriate title, and dimensions of 1200 pixels wide by 800 pixels tall
        self.__main_window = tk.Tk()

        self.__main_window.title("Movie Recommender")
        self.__main_window.geometry("1200x800")

        # notebook tab
        self.__notebook = ttk.Notebook(self.__main_window)
        self.__notebook.pack(expand=1, fill=tk.BOTH)


        # -----------  MOVIES TAB  -----------
        # Contains a notebook tab to display all of the movie titles and runtimes, as well as the movie statistics
        self.__movie_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__movie_tab, text="Movies")


        # This tab should be populated using the appropriate functions from the Recommender object

        self.__movie_text1 = tk.Text(self.__movie_tab, wrap="word")
        self.__movie_text2 = tk.Text(self.__movie_tab, wrap="word")

        # The user should be able to scroll through the title and runtimes
        self.__scrollbar = tk.Scrollbar(self.__movie_tab, command=self.__movie_text1.yview)
        self.__movie_text1.config(yscrollcommand=self.__scrollbar.set)

        # Packing text widget and scrollbar
        self.__movie_text2.pack(side=tk.BOTTOM, expand=1, fill=tk.BOTH)
        self.__scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.__movie_text1.pack(expand=1, fill=tk.BOTH)


        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        self.__movie_text1.insert(tk.END, "No data has been loaded yet")
        self.__movie_text2.insert(tk.END, "No data has been loaded yet")

        # The user should not be able to alter the data in the text areas
        self.__movie_text1.configure(state=tk.DISABLED)
        self.__movie_text2.configure(state=tk.DISABLED)


        # -----------  TV SHOW TAB  -----------
        # Contains a notebook tab to display all of the tv show titles and seasons, as well as the tv show statistics
        self.__tvshow_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tvshow_tab, text="TV shows")

        # This tab should be populated using the appropriate functions from the Recommender object
        self.__tvshow_text1 = tk.Text(self.__tvshow_tab, wrap="word")
        self.__tvshow_text2 = tk.Text(self.__tvshow_tab, wrap="word")

        # The user should be able to scroll through the title and seasons
        self.__scrollbar_text = tk.Scrollbar(self.__tvshow_tab, command=self.__tvshow_text1.yview)

        self.__tvshow_text1.config(yscrollcommand=self.__scrollbar_text.set)

        # Packing text widget and scrollbar
        self.__tvshow_text2.pack(side=tk.BOTTOM, expand=1, fill=tk.BOTH)
        self.__scrollbar_text.pack(side=tk.RIGHT, fill=tk.Y)
        self.__tvshow_text1.pack(expand=1, fill=tk.BOTH)



        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        self.__tvshow_text1.insert(tk.END, "No data has been loaded yet")
        self.__tvshow_text2.insert(tk.END, "No data has been loaded yet")

        # The user should not be able to alter the data in the text areas
        self.__tvshow_text1.configure(state=tk.DISABLED)
        self.__tvshow_text2.configure(state=tk.DISABLED)


        # -----------  BOOKS TAB  -----------
        # Contains a notebook tab to display all of the book titles and authors, as well as the book statistics

        self.__book_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__book_tab, text="Books")


        # This tab should be populated using the appropriate functions from the Recommender object

        self.__book_text1 = tk.Text(self.__book_tab, wrap="word")
        self.__book_text2 = tk.Text(self.__book_tab, wrap="word")

        # The user should be able to scroll through the title and authors
        self.__scrollbar = tk.Scrollbar(self.__book_tab, command=self.__book_text1.yview)
        self.__book_text1.config(yscrollcommand=self.__scrollbar.set)

        # packing text widget and scrollbar
        self.__book_text2.pack(side=tk.BOTTOM, expand=1, fill=tk.BOTH)
        self.__scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.__book_text1.pack(expand=1, fill=tk.BOTH)

        # If no data has been loaded yet, both text areas should display default text informing the user that no data has been loaded yet
        self.__book_text1.insert(tk.END, "No data has been loaded yet")
        self.__book_text2.insert(tk.END, "No data has been loaded yet")

        # The user should not be able to alter the data in the text areas
        self.__book_text1.configure(state=tk.DISABLED)
        self.__book_text2.configure(state=tk.DISABLED)


        # -----------  SEARCH MOVIES/TV SHOW TAB  -----------
        # Contains a notebook tab to allow the user to search through the movies and tv shows and should contain
        self.__search_mov_tv_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_mov_tv_tab, text="Search Movies/TV")

        # A Combobox with the options Movie and TV Show
        self.__type_option = ["Movie", "TV Show"]
        self.__type_combobox = ttk.Combobox(self.__search_mov_tv_tab, values=self.__type_option, state="readonly")


        # Appropriate Label and Entry widgets to collection information regarding the title, director, actor, and/or genre
        self.__type_label = tk.Label(self.__search_mov_tv_tab, text="Type: ")

        self.__title_label = tk.Label(self.__search_mov_tv_tab, text="Title: ")
        self.__title_field = tk.Entry(self.__search_mov_tv_tab, width=50)

        self.__director_label = tk.Label(self.__search_mov_tv_tab, text="Director: ")
        self.__director_field = tk.Entry(self.__search_mov_tv_tab, width=50)

        self.__actor_label = tk.Label(self.__search_mov_tv_tab, text="Actor: ")
        self.__actor_field = tk.Entry(self.__search_mov_tv_tab, width=50)

        self.__genre_label = tk.Label(self.__search_mov_tv_tab, text="Genre: ")
        self.__genre_field = tk.Entry(self.__search_mov_tv_tab, width=50)

        # packing all label and entry widgets
        self.__type_label.pack()
        self.__type_combobox.pack()

        self.__title_label.pack()
        self.__title_field.pack()

        self.__director_label.pack()
        self.__director_field.pack()

        self.__actor_label.pack()
        self.__actor_field.pack()

        self.__genre_label.pack()
        self.__genre_field.pack()

        # A Button to trigger the search, which calls the appropriate function from the Recommender object

        self.__mtv_search_button = tk.Button(self.__search_mov_tv_tab, text="Search", command=self.searchShows)
        self.__mtv_search_button.pack()

        # stores the results in the text area
        self.__search_mov_tv_text = tk.Text(self.__search_mov_tv_tab)
        # self.__search_mov_tv_text.pack(expand=1, fill=tk.BOTH)

        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
        self.__search_mov_tv_text.insert(tk.END, "Please enter data to perform the search")

        # The user should be able to scroll through the results
        self.__scrollbar_search_mtv = tk.Scrollbar(self.__search_mov_tv_tab, command=self.__search_mov_tv_text.yview)
        self.__search_mov_tv_text.config(yscrollcommand=self.__scrollbar_search_mtv.set)

        # packing text widget and scrollbar
        self.__scrollbar_search_mtv.pack(side=tk.RIGHT, fill=tk.Y)
        self.__search_mov_tv_text.pack(expand=1, fill=tk.BOTH)

        # The user should not be able to alter the data in the text area
        self.__search_mov_tv_text.configure(state=tk.DISABLED)


        # -----------  SEARCH BOOKS TAB  -----------
        # Contains a notebook tab to allow the user to search through the books and should contain

        self.__search_book_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_book_tab, text="Search Books")

        # Appropriate Label and Entry widgets to collection information regarding the title, author, and/or publisher

        self.__book_title_label = tk.Label(self.__search_book_tab, text="Title: ")
        self.__book_title_field = tk.Entry(self.__search_book_tab, width=50)

        self.__book_author_label = tk.Label(self.__search_book_tab, text="Author: ")
        self.__book_author_field = tk.Entry(self.__search_book_tab, width=50)

        self.__book_publisher_label = tk.Label(self.__search_book_tab, text="Publisher: ")
        self.__book_publisher_field = tk.Entry(self.__search_book_tab, width=50)

        # packing all label and entry widgets
        self.__book_title_label.pack()
        self.__book_title_field.pack()

        self.__book_author_label.pack()
        self.__book_author_field.pack()

        self.__book_publisher_label.pack()
        self.__book_publisher_field.pack()

        # A Button to trigger the search, which calls the appropriate function from the Recommender object and stores the results in the text area
        self.__book_search_button = tk.Button(self.__search_book_tab, text="Search", command=self.searchBooks)
        self.__book_search_button.pack()

        self.__book_search_text = tk.Text(self.__search_book_tab)
        
        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter data to perform a search
        self.__book_search_text.insert(tk.END, "Please enter data to perform the search")
        
        # The user should be able to scroll through the results
        self.__scrollbar_search_book = tk.Scrollbar(self.__search_book_tab, command=self.__book_search_text.yview)
        self.__book_search_text.config(yscrollcommand=self.__scrollbar_search_book.set)

        # packing text widget and scrollbar
        self.__scrollbar_search_book.pack(side=tk.RIGHT, fill=tk.Y)
        self.__book_search_text.pack(expand=1, fill=tk.BOTH)


        # The user should not be able to alter the data in the text area
        self.__book_search_text.configure(state=tk.DISABLED)


        # -----------  RECOMMENDATION TAB  -----------
        # Contains a notebook tab to allow the user to obtain media recommendations and should contain
        self.__recommendation_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__recommendation_tab, text="Recommendation")

        # A Combobox with the options Movie, TV Show, Book
        self.__rec_type_combobox = ttk.Combobox(self.__recommendation_tab, values=["Movie", "TV Show", "Book"], state="readonly")

        # Appropriate Label and Entry widgets to collection information regarding the title
        self.__rec_type_label = tk.Label(self.__recommendation_tab, text="Type: ")

        self.__rec_title_label = tk.Label(self.__recommendation_tab, text="Title: ")
        self.__rec_title_field = tk.Entry(self.__recommendation_tab, width=50)

        # packing input widgets
        self.__rec_type_label.pack()
        self.__rec_type_combobox.pack()
        self.__rec_title_label.pack()
        self.__rec_title_field.pack()

        # A Button to trigger the recommendation search, which calls the appropriate function from the Recommender object
        self.__rec_button = tk.Button(self.__recommendation_tab, text="Get Recommendation", command=self.getRecommendation)
        self.__rec_button.pack()

        # stores the results in the text area
        self.__rec_text = tk.Text(self.__recommendation_tab)

        # If no searches have been performed yet, the text areas should display some default text to inform the user they need to enter a title to receive a recommendation
        self.__rec_text.insert(tk.END, "Please enter data to perform the search")

        # The user should be able to scroll through the results
        self.__scrollbar_rec_text = tk.Scrollbar(self.__recommendation_tab, command=self.__rec_text.yview)
        self.__rec_text.config(yscrollcommand=self.__scrollbar_rec_text.set)

        # packing text widget and scrollbar
        self.__scrollbar_rec_text.pack(side=tk.RIGHT, fill=tk.Y)
        self.__rec_text.pack(expand=1, fill=tk.BOTH)


        # The user should not be able to alter the data in the text area
        self.__rec_text.config(state=tk.DISABLED)


        # -----------  Bonus Ratings TAB  -----------
        # tab called Ratings that will store two matplotlib pie charts. One pie chart will show each percentage of
        # ratings (G, PG, R, etc...) for movies, and the other pie charts will show the percentage of ratings for tv
        # shows. Be sure to include the label (G, PG, R, etc) and percentage value (with two decimals of precision) for
        # each slice of the pie chart. Note you will need to use a tkinter Canvas widget to display the pie charts.
        self.__rating_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__rating_tab, text="Ratings")

        self.__movie_ratings_label = tk.Label(self.__rating_tab, text="No shows data has been loaded yet")
        self.__movie_ratings_label.pack(expand=True)

        # -----------  MAIN BUTTONS  -----------
        # Buttons below the notebook that will have appropriate names and will:
        self.__button_frame = ttk.Frame(self.__notebook)

        # Load the show data using the loadShows()function
        self.__load_shows_button = tk.Button(self.__button_frame, text="Load Shows", command=self.loadShows)

        # Load the book data using the loadBooks()function
        self.__load_books_button = tk.Button(self.__button_frame, text="Load Books", command=self.loadBooks)

        # Load the association data using the loadAssociations()
        self.__load_association_button = tk.Button(self.__button_frame, text="Load Associations", command=self.loadAssociations)

        # Spawn a dialog containing the information regarding your team using the creditInfoBox()
        self.__information_button = tk.Button(self.__button_frame, text="Information", command=self.creditInfoBox)

        # Quit the program
        self.__quit_button = tk.Button(self.__button_frame, text="Quit", command=self.__main_window.destroy)

        self.__load_shows_button.pack(side=tk.LEFT, padx=50, pady=5)
        self.__load_books_button.pack(side=tk.LEFT, padx=50, pady=5)
        self.__load_association_button.pack(side=tk.LEFT, padx=50, pady=5)
        self.__information_button.pack(side=tk.LEFT, padx=50, pady=5)
        self.__quit_button.pack(side=tk.LEFT, padx=50, pady=5)

        self.__button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # --------  MAINLOOP  ----------
        self.__main_window.mainloop()

    # A loadShows() function that takes in no parameters, returns nothing, and:
        # Calls the appropriate function from the Recommender object to read in all of the data for the shows
        # Calls the appropriate function from the Recommender object to obtain the string representing the list of movies and the string representing the movie statistics and displays them in the appropriate text area
        # Calls the appropriate function from the Recommender object to obtain the string representing the list of tv shows and the string representing the tv show statistics and displays them in the appropriate text area
    def loadShows(self):
        self.__recommender.loadShows()

        movie_list = self.__recommender.getMovieList()
        movie_stats, movieRatings = self.__recommender.getMovieStats()
        tvshow_list = self.__recommender.getTVList()
        tvshow_stats, showRatings = self.__recommender.getTVStats()

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

        # TV show stuff

        if tvshow_list:
            self.__tvshow_text1.configure(state=tk.NORMAL)
            self.__tvshow_text1.delete(1.0, tk.END)
            self.__tvshow_text1.insert(tk.END, tvshow_list)
            self.__tvshow_text1.configure(state=tk.DISABLED)
        else:
            self.__tvshow_text1.configure(state=tk.NORMAL)
            self.__tvshow_text1.delete(1.0, tk.END)
            self.__tvshow_text1.insert(tk.END, "No data available")
            self.__tvshow_text1.configure(state=tk.DISABLED)

        if movie_stats:
            self.__tvshow_text2.configure(state=tk.NORMAL)
            self.__tvshow_text2.delete(1.0, tk.END)
            self.__tvshow_text2.insert(tk.END, tvshow_stats)
            self.__tvshow_text2.configure(state=tk.DISABLED)
        else:
            self.__tvshow_text2.configure(state=tk.NORMAL)
            self.__tvshow_text2.delete(1.0, tk.END)
            self.__tvshow_text2.insert(tk.END, "No statistics available")
            self.__tvshow_text2.configure(state=tk.DISABLED)

        # --------- Bonus: chart populating --------- #
        # emptying out Ratings tab Frame prior to adding charts
        for widget in self.__rating_tab.winfo_children():
            widget.destroy()

        matplotlib.use('TkAgg')
        plt.rcParams.update({'font.size': 7})

        # creating and adding Movie Ratings chart
        movieRatingLabels = list(movieRatings.keys())
        movieRatingSizes = list(movieRatings.values())
        movieRatingsChartFigure, movieCharAxes = plt.subplots(figsize=(4, 4))
        movie_wedges, _, movie_labels = movieCharAxes.pie(movieRatingSizes, labels=movieRatingLabels, autopct='%1.2f%%',
                                                          startangle=90)
        movieCharAxes.axis('equal')
        movieCharAxes.set_title("Movie Ratings")

        # Adjusting the position of each label
        for label, wedge in zip(movie_labels, movie_wedges):
            # Calculate the angle of the wedge's midpoint
            angle = (wedge.theta2 + wedge.theta1) / 2.0
            # Calculate the radius of the wedge
            radius = 0.7 * wedge.r
            # Calculate the x and y coordinates for label position
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # Set label position, vertical and horizontal alignment
            label.set_position((x, y))
            label.set_va('center')
            label.set_ha('center')
            # Adjust rotation angle for labels on the left side of the pie chart
            if angle > 90 and angle < 270:
                angle -= 180
            label.set_rotation(angle)
            # Set label background properties
            label.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='none'))

        # Draw the canvas
        canvas_movie_ratings = FigureCanvasTkAgg(movieRatingsChartFigure, master=self.__rating_tab)
        canvas_movie_ratings.draw()
        canvas_movie_ratings.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # creating and adding Shows Ratings chart
        movieRatingLabels = list(showRatings.keys())
        movieRatingSizes = list(showRatings.values())
        showRatingsChartFigure, showCharAxes = plt.subplots(figsize=(4, 4))
        tvshow_wedges, _, tvshow_labels = showCharAxes.pie(movieRatingSizes, labels=movieRatingLabels, autopct='%1.2f%%',
                                                         startangle=90)
        showCharAxes.axis('equal')
        showCharAxes.set_title("TV Show Ratings")

        # Adjusting the position of each label
        for label, wedge in zip(tvshow_labels, tvshow_wedges):
            # Calculate the angle of the wedge's midpoint
            angle = (wedge.theta2 + wedge.theta1) / 2.0
            # Calculate the radius of the wedge
            radius = 0.7 * wedge.r
            # Calculate the x and y coordinates for label position
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # Set label position, vertical and horizontal alignment
            label.set_position((x, y))
            label.set_va('center')
            label.set_ha('center')
            # Adjust rotation angle for labels on the left side of the pie chart
            if angle > 90 and angle < 270:
                angle -= 180
            label.set_rotation(angle)
            # Set label background properties
            label.set_bbox(dict(facecolor='white', alpha=0.5, edgecolor='none'))

        # Draw the canvas
        canvas_show_ratings = FigureCanvasTkAgg(showRatingsChartFigure, master=self.__rating_tab)
        canvas_show_ratings.draw()
        canvas_show_ratings.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    # A loadBooks() function that takes in no parameters, returns nothing, and:
    def loadBooks(self):
        # Calls the appropriate function from the Recommender object to read in all of the data for the books
        self.__recommender.loadBooks()

        # Calls the appropriate function from the Recommender object to obtain the string representing the list of books and the string representing the book statistics and displays them in the appropriate text area
        book_list = self.__recommender.getBookList()
        book_stats = self.__recommender.getBookStats()

        if book_list:
            self.__book_text1.configure(state=tk.NORMAL)
            self.__book_text1.delete(1.0, tk.END)
            self.__book_text1.insert(tk.END, book_list)
            self.__book_text1.configure(state=tk.DISABLED)
        else:
            self.__book_text1.configure(state=tk.NORMAL)
            self.__book_text1.delete(1.0, tk.END)
            self.__book_text1.insert(tk.END, "No data available")
            self.__book_text1.configure(state=tk.DISABLED)
        if book_stats:
            self.__book_text2.configure(state=tk.NORMAL)
            self.__book_text2.delete(1.0, tk.END)
            self.__book_text2.insert(tk.END, book_stats)
            self.__book_text2.configure(state=tk.DISABLED)
        else:
            self.__book_text2.configure(state=tk.NORMAL)
            self.__book_text2.delete(1.0, tk.END)
            self.__book_text2.insert(tk.END, "No data available")
            self.__book_text2.configure(state=tk.DISABLED)


    # A loadAssociations() function that takes in no parameters, returns nothing, and:
    def loadAssociations(self):
        # Calls the appropriate function from the Recommender object to read in all of the data for the associations
        self.__recommender.loadAssociations()


    # A creditInfoBox() function that takes in no parameters, returns nothing, and:
    def creditInfoBox(self):

        # Spawns a showinfo messagebox containing the names of each of your group members and what day the project was completed on
        message = "Author: Sahar and Samradnyee\nDate created: 4/23/24"
        messagebox.showinfo("Information", message)


    # A searchShows() function that takes in no parameters, returns nothing, and:
    def searchShows(self):
        # Extracts all of the data from the appropriate Combobox and Entry widgets to search for a movie or tv show
        type = self.__type_combobox.get()
        title = self.__title_field.get()
        director = self.__director_field.get()
        actor = self.__actor_field.get()
        genre = self.__genre_field.get()


        # Calls the appropriate function from the Recommender object to search for a movie or tv show, passing in the information from the Combobox and Entry widgets, and then displaying the returned string in the appropriate text area
        search_data = self.__recommender.searchTVMovies(type, title, director, actor, genre)

        if search_data:
            self.__search_mov_tv_text.configure(state=tk.NORMAL)
            self.__search_mov_tv_text.delete(1.0, tk.END)
            self.__search_mov_tv_text.insert(tk.END, search_data)
            self.__search_mov_tv_text.configure(state=tk.DISABLED)


    # A searchBooks() function that takes in no parameters, returns nothing, and:
    def searchBooks(self):
        # Extracts all of the data from the appropriate Entry widgets to search for a book
        title = self.__book_title_field.get()
        author = self.__book_author_field.get()
        publisher = self.__book_publisher_field.get()

        # Calls the appropriate function from the Recommender object to search for a book, passing in the information from the Entry widgets, and then displaying the returned string in the appropriate text area
        search_books_data = self.__recommender.searchBooks(title, author, publisher)

        if search_books_data:
            self.__book_search_text.configure(state=tk.NORMAL)
            self.__book_search_text.delete(1.0, tk.END)
            self.__book_search_text.insert(tk.END, search_books_data)
            self.__book_search_text.configure(state=tk.DISABLED)


    # A getRecommendations() function that takes in no parameters, returns nothing, and:
    def getRecommendation(self):
        # Extracts all of the data from the appropriate Combobox and Entry widgets,
        type = self.__rec_type_combobox.get()
        title = self.__rec_title_field.get()

        # Calls the appropriate function from the Recommender object to obtain recommendations, passing in the information from the Combobox and Entry widgets, and then displaying the returned string in the appropriate text area
        rec_data = self.__recommender.getRecommendations(type, title)

        if rec_data:
            self.__rec_text.configure(state=tk.NORMAL)
            self.__rec_text.delete(1.0, tk.END)
            self.__rec_text.insert(tk.END, rec_data)
            self.__rec_text.configure(state=tk.DISABLED)


def main():
    RecommenderGUI()

main()