from Assignment5.Book_Management_System import class_module

books = []

for i in range(5):
    print(f"\nEnter details of Book {i + 1}")

    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    price = float(input("Enter Price: "))

    book = class_module.Book(
        book_id,
        book_name,
        author,
        price
    )

    books.append(book)


print("\nAll Books:")
for book in books:
    book.display()

search_id = int(input("\nSearch Book Id: "))

found_book = None

for book in books:
    if book.book_id == search_id:
        found_book = book
        break

if found_book:
    print("\nBook Found:")
    found_book.display()
else:
    print("\nBook Not Found")


search_author = input("\nEnter Author Name: ")

print(f"\nBooks by {search_author}:")

for book in books:
    if book.author.lower() == search_author.lower():
        print(
            book.book_id,
            book.book_name,
            book.price
        )


print("\nBooks with price greater than 500:")

for book in books:
    if book.price > 500:
        print(book.book_name)


most_expensive = max(
    books,
    key=lambda book: book.price
)

print("\nMost Expensive Book:")
print(
    f"{most_expensive.book_name} = "
    f"{most_expensive.price:.0f}"
)


total_price = sum(book.price for book in books)
average_price = total_price / len(books)

print("\nAverage Price:")
print(average_price)
