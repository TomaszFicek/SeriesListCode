import sqlite3
import os
global rating_entering_sql
rating_entering_sql =0


def database_sql():

    global con
    con = sqlite3.connect('MoviesList_SQL.db')  # assigning to "con" value connection to "MovieList.db" database
    con.row_factory = sqlite3.Row  # access to to records of database by indexs and NAMES
    global cur
    cur = con.cursor()  # creating and assigning "cursor" methods to "cur" value

    cur.executescript(""" DROP TABLE IF EXISTS MoviesList;
    CREATE TABLE IF NOT EXISTS MoviesList (
                                                    id INTEGER PRIMARY KEY,
                                                    Movie_title varchar(50),
                                                    Rating INTEGER NOT NULL); """)
    cur.executemany("""INSERT INTO MoviesList (id, Movie_title, Rating) VALUES (?, ?, ?);""",
                    ((None, "The Shawshank Redemption", 9),
                     (None, "Intouchables", 9),
                     (None, "The Pianist", 8),
                     (None, "Joker", 8),
                     (None, "Braveheart", 7),
                     (None, "IronMan", 6),
                     (None, "Ice Age", 5),
                     (None, "American Sniper", 6),
                     (None, "Madagascar", 4),
                     (None, "The Lord of the Ring", 8)))


    cur.executescript(""" DROP TABLE IF EXISTS AmountMovieRating;
        CREATE TABLE IF NOT EXISTS AmountMovieRating (
                                                        id_ INTEGER,
                                                        Rating_amount INTEGER,
                                                        FOREIGN KEY(id_) REFERENCES MoviesList(id)); """)

    cur.execute(""" SELECT id FROM MoviesList """)
    id_ = cur.fetchall()

    for i in id_:
        cur.execute(""" INSERT INTO AmountMovieRating (id_, Rating_amount) VALUES (?, ?); """, (i["id"], 1))

    con.commit()


def movies_list_drawing():

    global con
    con = sqlite3.connect('MoviesList_SQL.db')
    con.row_factory = sqlite3.Row
    global cur
    cur = con.cursor()

    cur.execute(""" SELECT id, Movie_title FROM MoviesList """)
    MoviesList = cur.fetchall()

    LongestMovieTitle = 0
    for i in MoviesList:
        if len(i["Movie_title"]) > LongestMovieTitle:
            LongestMovieTitle = len(i["Movie_title"])

    print("\n", end="")
    if LongestMovieTitle % 2 == 0:
        print("|{}Movies{}|".format(" " * int((LongestMovieTitle - 3) / 2), " " * int((LongestMovieTitle - 3) / 2 + 1)))
    else:
        print("|{}Movies{}|".format(" " * int((LongestMovieTitle - 3) / 2), " " * int((LongestMovieTitle - 3) / 2)))

    print("*" * (LongestMovieTitle + 5))

    for i in MoviesList:
        if i["id"] < 10:
            print("{}{}{}".format("|" + str(i["id"]) + ".", " " + i["Movie_title"], " " *
                                  ((LongestMovieTitle + 4) - (len(i["Movie_title"]) + 4)) + "|"))
        else:
            print("{}{}{}".format("|" + str(i["id"]) + ".", " " + i["Movie_title"], " " *
                                  ((LongestMovieTitle + 3) - (len(i["Movie_title"]) + 4)) + "|"))
    print("\n", end="")


def wrtie_title():

    print("Please, add your title of Movie and its rating to the Series List")
    print("First, enter title of Movie and click enter button")
    global title_entering_sql
    title_entering_sql = input()
    print("You entered '{}' - type 'y' if entered title is correctly or type 'n' if you"
          " want to correct title".format(title_entering_sql.capitalize()))
    a = input()
    if a == "y":
        print("You added '{}' to the Movies list".format(title_entering_sql.capitalize()))
    elif a == "n":
        print("Enter title again:")
        title_entering_sql = input()
        print("You added '{}' to the Movies list".format(title_entering_sql.capitalize()))
    elif a != "y" or a != "n":
        print("Enter title again:")
        title_entering_sql = input()
        print("You added '{}' to the Movies list".format(title_entering_sql.capitalize()))

    rating_entering_sql
    write_rating(rating_entering_sql, title_entering_sql, write_rating, rewrite_rating)


def write_rating(rating_entering_sql, title_entering_sql, write_rating, rewrite_rating):

    global first_variable
    rating_entering_sql
    print("\nNow, please type rating of '{}' film - rate Movie from 1 to 10".format(title_entering_sql.capitalize()))
    try:
        rating_entering_sql = int(input())
        if rating_entering_sql in range(1, 11):
            print(
                "You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(), rating_entering_sql))
            first_variable = rating_entering_sql

            print("\n", end="")
        else:
            print("Entered rating is out of range 1:10, please type value from 1 to 10")
            if rating_entering_sql in range(1, 11):
                print(
                    "You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(),
                                                                    rating_entering_sql))
                first_variable = rating_entering_sql
                print("\n", end="")
            else:
                write_rating(rating_entering_sql, title_entering_sql, write_rating, rewrite_rating)

    except ValueError:
        rewrite_rating(rating_entering_sql, title_entering_sql, write_rating)


def rewrite_rating(rating_entering_sql, title_entering_sql, write_rating):

    global first_variable
    print("You mustn't rate movie as a char type. You must give value from 1 to 10 range.")
    print("Enter rating correctly:")
    try:
        rating_entering_sql = int(input())
        if rating_entering_sql in range(1, 11):
            print("You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(), rating_entering_sql))
            first_variable = rating_entering_sql
            print("\n", end="")
        else:
            print("Entered rating is out of range 1:10, please type value from 1 to 10")
            if rating_entering_sql in range(1, 11):
                print("You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(),
                                                                      rating_entering_sql))
                first_variable = rating_entering_sql
                print("\n", end="")
            else:
                write_rating(rating_entering_sql, title_entering_sql, write_rating, rewrite_rating)

    except ValueError:
        rewrite_rating(rating_entering_sql, title_entering_sql, write_rating)


def write_data_to_database():

    data_tuple = (None, title_entering_sql.capitalize(), first_variable)

    cur.execute("""INSERT INTO MoviesList (id, Movie_title, Rating) VALUES (?, ?, ?)""", (data_tuple))

    cur.execute(""" SELECT MAX(id) FROM MoviesList """)
    last_id = cur.fetchone()
    cur.execute(""" INSERT INTO AmountMovieRating (id_, Rating_amount) VALUES (?, ?); """, (last_id[0], 1))
    con.commit()


def add_movie_rating():

    print("\nPlease, give a number of movie title from below table which you want check its rating and adding your rating")

    movies_list_drawing()
    try:
        number_of_movie = input()

        global con
        con = sqlite3.connect('MoviesList_SQL.db')
        con.row_factory = sqlite3.Row
        global cur
        cur = con.cursor()

        cur.execute(""" SELECT id, Movie_title, Rating FROM MoviesList """)
        movie_id = cur.fetchall()

        if int(number_of_movie) in range(1, len(movie_id) + 1):
            for i in movie_id:
                if int(number_of_movie) == i["id"]:
                    print("You pick '{}' movie and its rating is {}/10".format(i["Movie_title"], i["Rating"]))

                    rating_entering_sql_2 = 0
                    write_rating(rating_entering_sql_2, i["Movie_title"], write_rating,
                                 rewrite_rating)
                    return
        else:
            print("Entered film number there isn't on movies list")
            add_movie_rating()
    except ValueError:
        print("You must give a number, not a char type value")
        add_movie_rating()


if os.path.isfile("MoviesList_SQL.db"):
    movies_list_drawing()
else:
    database_sql()
    movies_list_drawing()

wrtie_title()

write_data_to_database()

add_movie_rating() # should be change function inside a "add_movie_rating" (from "write-rating" to the new one which
# UPDATE database)



