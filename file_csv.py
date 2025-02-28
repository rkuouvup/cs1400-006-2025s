import csv
import operator

movie_csv = "move_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
      print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))

def sort_movie_data(data, index):
   header = data[0]
   sorted_movies = data[1:]
   if index == 3:
      sorted_movies.sort(key=get_money)
   else:
      sorted_movies.sort(key=operator.itemgetter(index))
   sorted_movies.insert(0, header)
   return sorted_movies

def get_money(gross):
   return float(gross[3][1:])

movie_data = fetch_movie_data(movie_csv) 
movie_data = sort_movie_data(movie_data, 3)
print_movie_data(movie_data)