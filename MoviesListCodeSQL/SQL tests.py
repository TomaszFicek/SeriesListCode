import sqlite3
import os



def database_sql():

    global con
    con = sqlite3.connect('MoviesList_SQL.db')  # assigning to "con" value connection to "MovieList.db" database
    con.row_factory = sqlite3.Row  # access to to records of database by indexs and NAMES
    global cur
    cur = con.cursor()  # creating and assigning "cursor" methods to "cur" value


    cur.executescript(""" DROP TABLE IF EXISTS MoviesList;
    CREATE TABLE IF NOT EXISTS MoviesList (
                                                    id INTEGER PRIMARY KEY,
                                                    Movie_title varchar(250),
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

    if LongestMovieTitle % 2 == 0:  #
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
        print("You added '{}' to the Series list".format(title_entering_sql.capitalize()))
    elif a != "y" or a != "n":
        print("Enter title again:")
        title_entering_sql = input()
        print("You added '{}' to the Series list".format(title_entering_sql.capitalize()))

    write_rating()

def write_rating():

    global rating_entering_sql
    print("\nNow, please type rating of entered Movie - rate Movie from 1 to 10")
    try:
        rating_entering_sql = int(input())
        if rating_entering_sql in range(1, 11):
            print(
                "You rated a '{}' series on {}/10 rating".format(title_entering_sql.capitalize(), rating_entering_sql))
            print("\n")
        else:
            print("Entered rating is out of range 1:10, please type value from 1 to 10")
            if rating_entering_sql in range(1, 11):
                print(
                    "You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(),
                                                                     rating_entering_sql))
                print("\n")
            else:
                write_rating()

    except ValueError:
        rewrite_rating()




def rewrite_rating():

    global rating_entering_sql
    print("You mustn't rate movie as a char type. You must give value from 1 to 10 range.")
    print("Enter rating correctly:")
    try:
        rating_entering_sql = int(input())
        if rating_entering_sql in range(1, 11):
            print("You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(), rating_entering_sql))
            print("\n")
        else:
            print("Entered rating is out of range 1:10, please type value from 1 to 10")
            if rating_entering_sql in range(1,11):
                print("You rated a '{}' movie on {}/10 rating".format(title_entering_sql.capitalize(),
                                                                      rating_entering_sql))
                print("\n")
            else:
                write_rating()

    except ValueError:
        rewrite_rating()


def write_data_to_database():

    data_tuple = (None, title_entering_sql.capitalize(), rating_entering_sql)
    print(data_tuple)
    print(type(data_tuple))

    cur.execute("""INSERT INTO MoviesList (id, Movie_title, Rating) VALUES (?, ?, ?)""", (data_tuple))
    con.commit()


if os.path.isfile("MoviesList_SQL.db"):
    print("true")
    movies_list_drawing()
else:
    print("false")
    database_sql()
    movies_list_drawing()


wrtie_title()

write_data_to_database()

"""

"""


