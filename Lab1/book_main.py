from book import Book

def main():
    python_book = Book("Intro to Python",
                       "Bill Smith",
                       12343213,
                       29.99,
                       "Programming",
                       15.67)
    java_book = Book("Intro to Java",
                     "Susan Smith",
                     23343213,
                     39.99,
                     "Programming",
                     25.67)

    print(python_book.get_description())
    print(java_book.get_description())
    print(f"Python profit is {python_book.get_profit():.2f}")
    print(f"Java profit is {java_book.get_profit():.2f}")

    python_book.change_price(24.99)

    python_book.add_review("Great book!")
    python_book.add_review("Lacking details on OOP")
    java_book.add_review("Good reference on Java")
    print(python_book.get_description())
    print(java_book.get_description())
    print(f"Python profit is {python_book.get_profit():.2f}")
    print(f"Java profit is {java_book.get_profit():.2f}")


if __name__ == "__main__":
    main()
