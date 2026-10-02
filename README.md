# GreenMart Customer Data Cleanup & Organizer

## Project Overview

The **GreenMart Customer Data Cleanup & Organizer** is a Core Python application designed to help a small business organize, search, sort, filter, and summarize customer records.

The project simulates a freelance client request from **GreenMart Supplies**, a fictional business that needs a simple tool for managing customer data without using a database or external libraries.

The application demonstrates how Python collections, functions, loops, conditionals, searching, sorting, filtering, and basic data-processing techniques can be combined to build a practical business application.

---

## Client Problem

GreenMart Supplies has customer records stored as Python data structures. Some records may be duplicated, and the business needs a simple way to:

* View customer records
* Search for individual customers
* Sort customers
* Filter customers by city
* Remove duplicate customer records
* Generate a summary of the customer data

The goal was to create a lightweight command-line solution using **Core Python only**.

---

## Features

The application provides the following menu options:

1. **Display Customers**

   * Displays all customer records.

2. **Search Customer**

   * Searches for a customer by name.
   * Returns the customer's name, city, and number of orders.
   * Handles customers who are not found.

3. **Sort Customers**

   * Sorts customers alphabetically by name.
   * Sorts customers by orders from highest to lowest.

4. **Filter Customers**

   * Filters customer records by city.
   * Handles cities with no matching customers.

5. **Remove Duplicates**

   * Identifies duplicate customers using their names.
   * Keeps the first occurrence of each customer.
   * Displays the original and unique record counts.

6. **Generate Summary**

   * Calculates total records.
   * Calculates unique customers.
   * Calculates total orders.
   * Counts customers by city.

7. **Exit**

   * Safely terminates the application.

---

## Technologies

* Python 3
* Core Python
* Lists
* Dictionaries
* Sets
* Tuples
* Functions
* Loops
* Conditional statements
* `sorted()`
* `lambda`
* `enumerate()`
* Command-line input/output

No external Python libraries are required.

---

## Project Structure

```text
customer-data-cleanup-organizer/
│
├── customer_data_cleanup_system.py
└── README.md
```

---

## Sample Customer Data

The application works with customer records stored as a list of dictionaries:

```python
customers = [
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8},
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Peter Kariuki", "city": "Nairobi", "orders": 3},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8}
]
```

This sample intentionally contains duplicate customer records so that the cleanup functionality can be demonstrated.

---

## How to Run

Clone or download the project and navigate to the project directory.

Run:

```bash
python customer_data_cleanup_system.py
```

The application will display the main menu:

```text
==================================================
 GreenMart Customer Data Organizer
==================================================

Select One Option

1. Display Customer
2. Search Customer
3. Sort Customers
4. Filter Customers
5. Remove Duplicates
6. Generate Summary
7. Exit
```

Select an option by entering the corresponding number.

---

## Example Summary

Using the sample customer data, the summary function produces:

```text
========================================
           CUSTOMER SUMMARY
========================================
Total Records: 5
Unique Customers: 4
Total Orders: 29

Customers per City:
Nairobi: 3
Meru: 2
```

---

## Python Concepts Demonstrated

This project was developed as a practical application of Core Python concepts.

### Lists

A list is used to store the collection of customer records.

```python
customers = [
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5}
]
```

### Dictionaries

Each customer is represented by a dictionary containing:

* `name`
* `city`
* `orders`

### Sets

A set is used when removing duplicate customer names:

```python
set_name = set()
```

The set allows efficient membership checking.

### Functions

The application is divided into reusable functions:

```text
display_customers()
display_menu()
remove_duplicates()
search_customer()
sort_customers()
filter_customers()
generate_summary()
```

### Searching

The `search_customer()` function iterates through the customer records and returns the matching customer.

### Sorting

The `sort_customers()` function uses Python's `sorted()` function and a `lambda` expression to specify the sorting field.

### Filtering

The `filter_customers()` function creates a new list containing customers from the requested city.

### Function Composition

The `generate_summary()` function reuses:

```python
remove_duplicates(customers)
```

instead of duplicating the duplicate-removal logic.

### Menu-Driven Programming

A `while` loop controls the application and allows the user to perform multiple operations until selecting **Exit**.

---

## Testing

The completed application was manually tested using the following scenarios:

* Displaying all customer records
* Searching for an existing customer
* Searching for a customer who does not exist
* Sorting customers by name
* Sorting customers by number of orders
* Filtering customers by an existing city
* Filtering by a city with no matching customers
* Removing duplicate records
* Generating the customer summary
* Exiting the application
* Entering an invalid menu option

All tested functions produced the expected results.

---

## Known Limitations

This project intentionally uses simple Core Python structures and therefore has several limitations:

* Customer data is stored directly in the Python program.
* Data is not saved to a database.
* The application does not currently read customer records from CSV files.
* Input validation is basic.
* Customer identity for duplicate detection is based on the customer's name.
* The application is command-line based.
* No external libraries are used.

These limitations are intentional because the project focuses on demonstrating Core Python and collection-handling skills.

---

## Possible Future Improvements

The application could later be extended to include:

* CSV file import and export
* More robust input validation
* Persistent data storage
* Database integration
* REST API integration
* Pandas-based data processing
* Automated unit testing
* A graphical or web interface
* Larger customer datasets

These improvements would be appropriate as the project progresses into more advanced Python, databases, APIs, and data-processing topics.

---

## Learning Objectives

This project was created to demonstrate practical competency in:

* Working with Python collections
* Designing reusable functions
* Breaking a problem into smaller components
* Searching and filtering data
* Sorting collections
* Removing duplicate records
* Calculating summaries
* Combining multiple functions into a working application
* Building a menu-driven command-line program
* Testing and debugging a Python application

---

## Project Status

**Completed — Core Python Version**

The current version successfully implements the required customer data cleanup and organization features using Core Python.

---

## Author

**Gibson Muthuri**

This project is part of a practical Python learning and portfolio-development journey focused on building real-world applications through project-based learning.
