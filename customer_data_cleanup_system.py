customers = [
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8},
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "GPeter Kariuki", "city": "Nairobi", "orders": 3},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8}
]
#Function to display all customers record
def display_customers(customers):
    for number, customer in enumerate(customers, start=1):
            print(f"{number}. Customer Name: {customer['name']}")
            print(f"   City: {customer['city']}")
            print(f"   Orders: {customer['orders']}")

#function to display menu for users
def display_menu():
    print(f"{ '=' * 50}")
    print(" GreenMart Customer Data Organizer")
    print(f"{ '=' * 50}")
    print()
    print("Select One Option")
    print()
    print("1. Display Customer")
    print("2. Search Customer")
    print("3. Sort Customers")
    print("4. Filter Customers")
    print("5. Remove Duplicates")
    print("6. Generate Summary")
    print("7. Exit")      

#function to remove duplicate from list
def remove_duplicates(customers):
    unique_customer = []
    set_name = set()

    for customer in customers:
        if customer["name"] in set_name:
            continue
        else:
            unique_customer.append(customer)
            set_name.add(customer["name"])

    return unique_customer

#function to search from customer list
def search_customer(customers, customer_name):
    for customer in customers:
        if customer["name"] == customer_name:
            return customer
    return None

#function to sort by name and order
def sort_customers(customers, sort_criterion):
    if sort_criterion == "name":
        return sorted(customers, key=lambda customer: customer["name"])
    elif sort_criterion == "orders":
        return sorted(customers, key=lambda customer: customer["orders"], reverse=True)

#funtion to filter by city option
def filter_customers(customers, filter_criterion):
    filtered_customer = []
    for customer in customers:
        if customer["city"] == filter_criterion:
            filtered_customer.append(customer)
    return filtered_customer

#function to give summary
def generate_summary(customers):
    total_orders = 0
    customers_per_city = {}

    unique_customers = remove_duplicates(customers)

    for customer in customers:
        city = customer["city"]

        if city in customers_per_city:
            customers_per_city[city] = customers_per_city[city] + 1
        else:
            customers_per_city[city] = 1

        total_orders = total_orders + customer["orders"]

    return len(customers), len(unique_customers), total_orders, customers_per_city
    

#Main Program
while True:
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
            display_customers(customers)
    elif choice == "2":
        customer_name = input("Enter customer name: ")
        result = search_customer(customers, customer_name)

        if result is None:
            print("Customer is not found")
        else:
            print("Name:", result["name"])
            print("City:", result["city"])
            print("Orders:", result["orders"]) 
    elif choice == "3":
        print("1. Sort by Name (A-Z)")
        print("2. Sort by Orders (Highest to Lowest)")

        sort_choice = input("Enter sorting choice: ")

        if sort_choice == "1":
            sorted_customers = sort_customers(customers, "name")
            display_customers(sorted_customers)

        elif sort_choice == "2":
            sorted_customers = sort_customers(customers, "orders")
            display_customers(sorted_customers)

        else:
            print("Invalid sorting choice.")
    elif choice == "4":
        city = input("Enter city to filter by: ")

        filtered_customers = filter_customers(customers, city)

        if filtered_customers:
            display_customers(filtered_customers)
        else:
            print("No customers found in that city.")
    elif choice == "5":
        unique_customers = remove_duplicates(customers)

        print("Duplicate records removed.")
        print(f"Original records: {len(customers)}")
        print(f"Unique records: {len(unique_customers)}")

        display_customers(unique_customers)

    elif choice == "6":
        summary = generate_summary(customers)

        print("========================================")
        print("           CUSTOMER SUMMARY")
        print("========================================")

        print("Total Records:", summary[0])
        print("Unique Customers:", summary[1])
        print("Total Orders:", summary[2])

        print("\nCustomers per City:")

        for city, count in summary[3].items():
            print(f"{city}: {count}")
    elif choice == "7":
        print("Thank you for using GreenMart Customer Data Organizer.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")