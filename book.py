class Book:
    def __init__(self, title, author, prices):
        self.id = title.replace(" ", "") .lower()
        self.title = title
        self.author = author

        self.copies = []
        for no, price in enumerate(prices, 1):

            self.copies.append({
                "id": f"{self.id}{no:03}",
                "price": price,
                "available": True,
                "scanned_count": 0,
                "lent_count": 0,
                "returned_count": 0
            })

    def __str__(self):
        book_copy = []
        for copy in self.copies:
            status = "Available" if copy["available"] else "Not Available"
            book_copy.append(f"{copy["id"]} - ${copy["price"]} - {status}")
        return f"Book: {self.title}, {self.author} : {book_copy}"
