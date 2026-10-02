# Customer Data Cleanup & Organizer

A Core Python portfolio project developed for a fictional small wholesale and retail business, **GreenMart Supplies**.

The project demonstrates how Python can be used to clean, organize, search, filter, sort, and summarize customer records stored as a list of dictionaries.

## Project Overview

GreenMart Supplies maintains customer information in a simple Python data structure. The business needs a small utility that can help staff organize customer records and quickly retrieve useful information.

The system provides functions for:

* Displaying customer records
* Searching for a customer
* Sorting customers by name
* Sorting customers by number of orders
* Filtering customers by city
* Removing duplicate customer records
* Generating a summary of the customer data

This project is intentionally built using **Core Python** to demonstrate fundamental programming skills before introducing external libraries, databases, or APIs.

## Client Requirements

The system should work with customer records containing:

* Customer name
* City
* Number of orders

Example:

```python
customers = [
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8},
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Peter Kariuki", "city": "Nairobi", "orders": 3},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8}
]
```

## Features

### 1. Display Customers

Displays customer records in a readable format.

```python
display_customers(customers)
```

### 2. Search Customers

Searches for a customer by name and returns the matching customer record.

```python
search_customer(customers, customer_name)
```

If no customer is found, the function returns `None`.

### 3. Sort Customers

Customers can be sorted by:

* Name — A to Z
* Number of orders — highest to lowest

```python
sort_customers(customers, sort_criterion)
```

### 4. Filter Customers

Filters customers based on their city.

```python
filter_customers(customers, filter_criterion)
```

For example:

```text
Nairobi
```

returns only customers located in Nairobi.

### 5. Remove Duplicates

Removes duplicate customer records based on customer name while keeping the first occurrence.

```python
remove_duplicates(customers)
```

### 6. Generate Summary

Generates useful information about the customer dataset, including:

* Total number of records
* Number of unique customers
* Total orders
* Number of customers per city

```python
generate_summary(customers)
```

## Technologies Used

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
* Lambda functions
* File handling
* Basic data processing

## Project Structure

```text
customer-data-cleanup-organizer/
│
├── customer_data.py
├── main.py
├── README.md
└── tests/
    └── test_customer_data.py
```

> The exact file structure may change as the project develops.

## Learning Objectives

This project demonstrates practical understanding of:

1. Working with lists of dictionaries
2. Accessing dictionary values
3. Iterating through collections
4. Using sets to identify duplicates
5. Searching data
6. Sorting structured data
7. Filtering data
8. Designing reusable functions
9. Returning values from functions
10. Separating data processing from display logic
11. Testing normal and boundary cases
12. Writing documentation for a software project

## Example Results

### Search

Searching for:

```text
Mary Wanjiku
```

Expected result:

```text
{'name': 'Mary Wanjiku', 'city': 'Meru', 'orders': 8}
```

### Sort by Orders

Expected order:

```text
Mary Wanjiku - 8 orders
John Mwangi - 5 orders
Peter Kariuki - 3 orders
```

### Filter by City

Filtering by:

```text
Nairobi
```

returns customers located in Nairobi.

## Testing

The project will be tested using normal, boundary, and invalid/no-match cases.

Examples include:

* Searching for an existing customer
* Searching for a customer who does not exist
* Sorting by name
* Sorting by orders
* Filtering by an existing city
* Filtering by a city with no customers
* Removing duplicate records
* Verifying that the original customer list is not unexpectedly modified

Testing results and screenshots will be added as the project progresses.

## Current Limitations

This is an intentionally simple Core Python project.

It currently does not include:

* Database storage
* REST APIs
* Pandas or NumPy
* Web scraping
* Graphical user interface
* User authentication
* Advanced input validation
* Large-scale data processing

These limitations are intentional because the project is designed to demonstrate Python fundamentals and data-collection processing.

## Future Improvements

Possible future versions could include:

* CSV file import and export
* Stronger data validation
* Database storage
* REST API integration
* Pandas-based data analysis
* Web interface
* Automated testing
* Larger datasets

## Project Status

**In Development**

The project is being developed incrementally, with each function designed, implemented, tested, and documented before moving to the next component.

## Author

**Gibson Muthuri**

Python / AI Development Portfolio

---

### Portfolio Context

This project is part of a practical Python learning portfolio focused on developing programming competency through realistic, client-oriented problems.

The objective is not only to produce working code, but also to practice:

**Understanding requirements → Designing a solution → Writing modular code → Testing → Documenting → Delivering**
