from book import Book
import json


class Library:

    books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only books can be added")

    def load_book_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                title = item.get("title")
                author = item.get("author")
                prices = item.get("prices")
                if title and prices:
                    book = Book(title, author, prices)
                    self.add_book(book)

    def check_library(self):
        for book in self.books:
            print(book)

    def scanned_book(self, tag):
        for book in self.books:
            for copy in book.copies:
                if copy["id"] == tag:
                    copy["scanned_count"] += 1
                    print(
                        f"{book.title}: {copy["id"]} - Price: ${copy["price"]}")

    def lend_a_book(self, tag):
        for book in self.books:
            for copy in book.copies:
                if copy["id"] == tag:
                    if copy["available"]:
                        copy["available"] = False
                        copy["lent_count"] += 1
                        print(
                            f"{book.title}: {copy["id"]} has been Checked out to a member")
                        return
                    else:
                        print(f"{book.title} currently not available")
                    return
        print(f"{book.title} book doesn't exist in the library")

    def book_returned(self, tag):
        for book in self.books:
            for copy in book.copies:
                if copy["id"] == tag:
                    if not copy["available"]:
                        copy["available"] = True
                        copy["returned_count"] += 1
                        print(f"{book.title} has been returned and now available")
                    else:
                        print(
                            f"{book.title}: {copy["id"]} never left the library")
                    return
        print("This book doesn't exist in the library")

    def analysis_per_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():

                print(f"Book Analysis: {book.title}")
                print(f"Book Author: {book.author}")
                print("-" * 60)
                total_scanned = 0
                total_lent = 0
                total_returned = 0
                total_price = 0
                available_count = 0

                for copy in book.copies:
                    print(
                        f"Copies: {copy["id"]} | Scanned: {copy["scanned_count"]} | Lent: {copy["lent_count"]} | Returned: {copy["returned_count"]} | Price: ${copy["price"]} | Availability:{copy["available"]}")

                    total_scanned += copy["scanned_count"]
                    total_lent += copy["lent_count"]
                    total_returned += copy["returned_count"]
                    total_price += copy["price"]
                    if copy["available"]:
                        available_count += 1

                print("Summary")
                print(f"Total Copies: {len(book.copies)}")
                print(f"Total Scans: {total_scanned}")
                print(f"Total lent: {total_lent}")
                print(f"Total Returns: {total_returned}")
                print(f"Total Asset Value: ${total_price}")
                print(f"Total Available: {available_count}")

    def analysis(self):
        for book in self.books:
            for copy in book.copies:
                print(
                    f"Book - {book.title}, ID: {copy["id"]}, Scanned: {copy["scanned_count"]}, Lent: {copy["lent_count"]}, Returned: {copy["returned_count"]}, Price: ${copy["price"]}, Current_availability: {copy["available"]}")


lib = Library()
# lib.add_book(Book("Walking dead", [150, 160]))
# lib.add_book(Book("Water ways", [90, 90]))
lib.load_book_json("book.json")
# lib.check_library()
# lib.scanned_book("elonmusk001")
# lib.lend_a_book("elonmusk001")
# lib.lend_a_book("elonmusk002")
# lib.book_returned("elonmusk001")
# # lib.lend_a_book("elonmusk001")
# lib.analysis_per_book("Elon Musk")
lib.analysis()
