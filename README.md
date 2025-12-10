# Library Management System (Python)

This project is a Python-based Library Management System designed to simulate how a physical library or bookstore operates. It allows an admin to track books, manage multiple copies, scan items, lend and return books, and analyze usage data all from a single system.

The goal of this project is to model a real-world physical library where each book can have multiple unique copies, each with its own price, availability status, and activity history.

## Project Architecture Overview

The system is built using **Object-Oriented Programming (OOP)** and is divided into two main components:
*Book* → Handles individual book data and copies
*Library* → Manages the entire collection and all operations
*book.json* → Acts as persistent storage for loading books into the system

### Book Class — Managing Individual Books & Copies

```python

class Book:
```
The *Book* class represents a single book title and automatically creates unique copies based on the prices provided.

**Key Features:**
- Each book gets a unique ID based on its title.
- Each copy gets its own:
    - Unique copy ID
    - Price
    - Availability status
    - Scan count
    - Lending count
    - Return count

**Constructor Breakdown**

```python

def __init__(self, title, author, prices):
```
When a book is created:
*title* → Name of the book
*author* → Book author
*prices* → A list of prices (each price = one physical copy)

Each copy is automatically created like this:

```python

self.copies.append({
    "id": f"{self.id}{no:03}",
    "price": price,
    "available": True,
    "scanned_count": 0,
    "lent_count": 0,
    "returned_count": 0
})
```

**Displaying Book Information**

```python

def __str__(self):
```
This method allows each book to be printed in a clean, readable format:
- Shows title
- Shows author
- Lists all copies
- Displays availability and prices
This makes it easy for the admin to quickly check inventory.

### Library Class — Core System Controller

```python

class Library:
```

This class manages everything in the system:
- Book storage.
- Scanning.
- Lending.
- Returning.
- Full analysis.

All books are stored in:

```python

books = []
```
**Adding Books**

```python

def add_book(self, book):
```
- Ensures only valid Book objects can be added.
- Prevents invalid data from entering the system.

**Loading Books from JSON**

```python

def load_book_json(self, filename):
```    
This function loads books from a JSON file.
Extracts:Title, Author and Prices.
Automatically converts each record into a Book object
*This allows the system to behave like a real database-powered application, even though it uses JSON.*

**Checking Library Inventory**

```python

def check_library(self):
```
Displays all books and all their copies in the system.

**Scanning a Book**

```python

def scanned_book(self, tag):
```
Accepts a unique copy ID
Increments on the scan count
Displays the book title and price
*This simulates barcode scanning at a physical counter.*

**Lending a Book**

```python

def lend_a_book(self, tag):
```
Checks if the book copy exists.
Confirms availability status.
Marks it as unavailable if not. 
Increments on lending count.
It Prevents double lending and lending unavailable books.

**Returning a Book**

```python

def book_returned(self, tag):
```
Marks the copy as available again.
Increments on the return count.
Prevents invalid returns.

**Per-Book Analysis (Admin Dashboard)**

```python

def analysis_per_book(self, title):
```
This function generates a full performance report for a single book, including:
- All copies
- Scans per copy
- Lending activity
- Return activity
- Total asset value
- Availability count
And also summarises metrics generated: Total copies, Total scans, Total times lent, Total returns, Total asset value, and Total available copies.
*This is exactly the kind of analytics an actual library admin would need.*

**Full Library Analysis**

```python

def analysis(self):
```
This method prints a complete system-wide report, showing: Every book, Every copy, Scan counts, Lending counts, Return counts, Prices and Current availability.
*This acts like a master audit report.*
