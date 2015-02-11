## movie_database.py

import csv

class Movie:      
##
##    with open("imdb_top250.csv", encoding='utf-8') as file:
##        reader = csv.reader(file)
##        for row in reader:
##            imdb_id = row[0]
##            title = row[1]
##            director = row[2]
##            rating = row[3]
##            year = row[4]
##            
##            
    def find_highest_rated(rates):
        with open("imdb_top250.csv", encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                imdb_id = row[0]
                title = row[1]
                director = row[2]
                rating = row[3]
                year = row[4]
                if rating > 9:
                    print(title)
            










