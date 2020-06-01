######################################################################

def series_list_drawing(): # declaration draw Series list function

    if ListWidth % 2 == 0:  #
        print("|{}Series{}|".format(" " * int((ListWidth - 3) / 2), " " * int((ListWidth - 3) / 2 + 1)))  #
    else:  #
        print("|{}Series{}|".format(" " * int((ListWidth - 3) / 2), " " * int((ListWidth - 3) / 2)))  #

# Above is drawing first line of Series list. Width first line of list is depend on longest element of "z" LIST type..
# ..object. If the longest element of "z" LIST contains even number of characters, first line of Series List is ...
# .. different than when  the longest element of "z" LIST contains odd number of characters.

    print("*" * (ListWidth + 5))  # Drawing stars line

    j = 1  # Filling out the Series List with KEYS from....
    for i in z:  # .. DICTIONARY type ("z" variable is e LIST with series title) OBJECT and drawing next lines..
        if j < 10:
            print("{}{}{}".format("|" + str(j) + ".", " " + str(i), " " * ((ListWidth + 4) - (len(i) + 4)) + "|"))  #..
            j += 1  # ..of Series List...If condition to width of list was the same independent from length of...
            # ...string in each row
        else:
            print("{}{}{}".format("|" + str(j) + ".", " " + str(i), " " * ((ListWidth + 3) - (len(i) + 4)) + "|"))
            j += 1

def title_typing():  # declaration title entering function

    print("Below there is a list of available series:\n")
    series_list_drawing()
    print("\n")
    global chosen_series  # change LOCAL VARIABLE  to GLOBAL  variable
    print("Please, chose one Series which you want see be typing it's title:")
    chosen_series = input()


def series_rating():  # declaration function which finds entered series title and displays its rating

    global chosen_series
    for i in z:
        if chosen_series == i:
            print("You picked a \"{}\" and its rating is:\t{}".format(chosen_series, ListSeries[chosen_series]))

            return
    title_retyping()    # calling a "title_retyping" function


def title_retyping():   # declaration a "title_retyping" function

    global chosen_series
    print("You entered title that there isn't on the Series List or you did mistake during entering title.\nPlease,"
          "look at below Series list again and enter correct title\n")
    series_list_drawing()   # calling a "series_list_drawing" function
    print("\n", end="")
    chosen_series = input()
    series_rating()


def read_file_with_series(): # declaration of function for opening "txt" file with list of series and for creating...
    # ...dictionary (dict) object - keys of dict object are series titles and values of dict object are series ratings

    global ListSeries  # change LOCAL VARIABLE  to GLOBAL  variable
    with open("SeriesList.txt", "r", encoding="utf-8") as SeriesListFile: # METHOD to OPEN..
        # ..file "SeriesList.txt". As a argument of OPEN method are: first - file name + its filename extension; second.
        # ..-open file mode (r,w or a);then encoding type. Then after "as" word need to be declare HANDLE  to opened...
        # ...file (name if this HANDLE)
        b = SeriesListFile.read()  # READ function is used for reading file content. To "b" value is assign content...
        # ..file - this content file is a string type
        b = b.split(",")  # creating a LIST object "b"
        l = b[::2]  # creating a "l" LIST object from list "b" elements (every second element starting with 0 index
        k = b[1::2]   # creating a "k" LIST object from list "b" elements (every second element starting with 1 index
        ListSeries = dict(zip(l, k))  # ZIP function crates a TUPLE objects from list "l" and list "k" - first TUPLE..
        # ..is created of first elements "l" and "k" lists. Next tuples are created of next element of list "l" and "k".
        # ...DICT function creates DICTIONARY object from earlier made TUPLE objects. This DICT object is assign to...
        # ..."ListSeries" value.


def write_to_file_title(): # function to write "series title" to txt file
    global title_entering
    print("Please, add your title of Series and its rating to the Series List")
    with open("SeriesList.txt", "a", encoding="utf-8") as SeriesFile:
        print("First, enter title of Series and click enter button")
        title_entering = input()
        print("You entered '{}' - type 'y' if entered title is correctly or type 'n' if you"
              " want to correct title".format(title_entering.capitalize()))
        a = input()
        if a == "y":
            print("You added '{}' to the Series list".format(title_entering.capitalize()))
            SeriesFile.write(title_entering.replace(title_entering, title_entering+",").capitalize())
        elif a == "n":
            print("Enter title again:")
            title_entering = input()
            print("You added '{}' to the Series list".format(title_entering.capitalize()))
            SeriesFile.write(title_entering.replace(title_entering, title_entering+",").capitalize())
    write_to_file_rating()


def write_to_file_rating(): # function to write "series rating" to txt file
    print("\nNow, please type rating of entered series - rate series from 1 to 10")
    with open("SeriesList.txt", "a", encoding="utf-8") as SeriesFile:
        try:
            rating_entering = int(input())
            if rating_entering in range(1, 11):
                print("You rated a '{}' series on {}/10 rating".format(title_entering.capitalize(), rating_entering))
                SeriesFile.write(str(rating_entering) + "/10,")
                print("\n")
            else:
                print("Entered rating is out of range 1:10, please type value from 1 to 10")
                rating_entering = int(input())
                print("You rated a '{}' series on {}/10 rating".format(title_entering.capitalize(), rating_entering))
                SeriesFile.write(str(rating_entering) + "/10,")
                print("\n")
        except ValueError:
            rewrite_to_file_rating()


def rewrite_to_file_rating(): # function to REwrite "title rating" in the case when user enter a CHAR type value
    print("You mustn't rate series as a char type. You must give value from 1 to 10 range.")
    print("Enter rating correctly:")
    with open("SeriesList.txt", "a", encoding="utf-8") as SeriesFile:
        try:
            rating_entering = int(input())
            if rating_entering in range(1, 11):
                print("You rated a '{}' series on {}/10 rating".format(title_entering.capitalize(), rating_entering))
                SeriesFile.write(str(rating_entering) + "/10,")
                print("\n")
            else:
                print("Entered rating is out of range 1:10, please type value from 1 to 10")
                rating_entering = int(input())
                print("You rated a '{}' series on {}/10 rating".format(title_entering.capitalize(), rating_entering))
                SeriesFile.write(str(rating_entering) + "/10,")
                print("\n")
        except ValueError:
            rewrite_to_file_rating()


read_file_with_series()  # Calling a "read_file_with_series" function

AllSeries = str(ListSeries.keys())      # .KEYS function creates list of all keys of object "ListSeries" (this list...
                                        # ..is a DICT_KEYS type. Then this list is change to string (str) type and ...
                                        # ..it is assign to "AllSeries variable
AllSeriesClean= AllSeries.lstrip("dict_keys(['")   # .LSTRIP/RIGHT function deletes from start/end of string...
AllSeriesClean = AllSeriesClean.rstrip("])")       # ... "AllSeries" characters, which are argument of STRIP function...
                                                    # ..and than this new string is assign to variable "AllSeriesClean"

AllSeriesCleanClean = AllSeriesClean.replace("'", "") # Deleting of "'" characters from "AllSeriesClean" string...
                                                    # ..and assigning it to "AllSeriesCleanClean" variable
AllSeriesCleanCleanClean = AllSeriesCleanClean.replace(", ", ",") # Change ", " to ","
z = AllSeriesCleanCleanClean.split(",") # Creating LIST type OBJECT from string by SPLIT function and assigning it to..
                                        # .. "z" variable

ListWidth = 0              #
for i in z:             # Searching the longest element from "z" LIST by LEN function. Each element of "z" LIST is ...
    if len(i) > ListWidth: # ..checked thanks FOR loop and the longest element is assigning to "ListWidth" variable
        ListWidth = len(i) #


print("\n")
print("Below there is a list of available series:\n") # Displaying a characters

series_list_drawing()  # Calling a "series_list_drawing" function
print("\n")
write_to_file_title()

title_typing()  # Calling a "title_typing" function

series_rating()  # Calling a "series_rating" function

