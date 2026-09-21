from Assignment7.Movie_Collection_System import class_module

movies = []

for i in range(5):
    print(f"\nEnter details of Movie {i + 1}")

    movie_id = int(input("Enter Movie ID: "))
    movie_name = input("Enter Movie Name: ")
    genre = input("Enter Genre: ")
    rating = float(input("Enter Rating: "))
    ticket_price = float(input("Enter Ticket Price: "))

    movie = class_module.Movie(
        movie_id,
        movie_name,
        genre,
        rating,
        ticket_price
    )

    movies.append(movie)


print("\nAll Movies:")
for movie in movies:
    movie.display()

print("\nMovies with rating greater than 8:")

for movie in movies:
    if movie.rating > 8:
        print(movie.movie_name, movie.rating)


print("\nAction Movies:")

for movie in movies:
    if movie.genre.lower() == "action":
        print(movie.movie_name)


highest_rated_movie = max(
    movies,
    key=lambda movie: movie.rating
)

print("\nHighest Rated Movie:")
print(
    highest_rated_movie.movie_name,
    highest_rated_movie.rating
)


search_id = int(input("\nSearch Movie Id: "))

found_movie = None

for movie in movies:
    if movie.movie_id == search_id:
        found_movie = movie
        break

if found_movie:
    print("\nMovie Found:")
    found_movie.display()
else:
    print("\nMovie Not Found")


total_rating = sum(movie.rating for movie in movies)
average_rating = total_rating / len(movies)

print("\nAverage Movie Rating:")
print(f"{average_rating:.2f}")


print("\nMovies with ticket price greater than 300:")

for movie in movies:
    if movie.ticket_price > 300:
        print(
            movie.movie_name,
            movie.ticket_price
        )
