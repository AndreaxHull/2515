class Book:
    """ Represents a book in an online bookstore """

    def __init__(self, book_title, author, isbn, price, genre, cost):
        """ Initialize our book """
        self._title = book_title
        self._author = author
        self._isbn = isbn
        self._genre = genre

        if price <= 0.0:
            raise ValueError("Price must be positive")
        self._price = price

        if cost > price:
            raise ValueError("Cannot sell for a loss")
        self._cost = cost

        self._reviews = []

    def change_price(self, new_price):
        """ Change the current price of the book """
        if new_price <= 0.0:
            raise ValueError("Price must be positive")
        self._price = new_price

    def get_profit(self):
        """ Return the expected profit for a sale of the book """
        return self._price - self._cost

    def add_review(self, review_text):
        """ Adds a review to the book """
        self._reviews.append(review_text)

    def get_description(self):
        """ Returns a string with a summary of the book info """
        desc = f"{self._title} by {self._author} (ISBN: {self._isbn}) with genre of {self._genre} " \
               f"selling for ${self._price:.2f} with {len(self._reviews)} reviews"
        return desc
