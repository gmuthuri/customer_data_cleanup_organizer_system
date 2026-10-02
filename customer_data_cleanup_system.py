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
    
customers = [
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8},
    {"name": "John Mwangi", "city": "Nairobi", "orders": 5},
    {"name": "GPeter Kariuki", "city": "Nairobi", "orders": 3},
    {"name": "Mary Wanjiku", "city": "Meru", "orders": 8}
]

#search output
print("SEARCH BY NAME")
result = search_customer(customers, "Peter Kariuki")
if result is None:
    print("Customer is not found")
else:
    print("Name:", result["name"])
    print("City:", result["city"])
    print("Orders:", result["orders"])
print(f"{ '+' * 50}")

#cleaned list with no duplicate
print("CUSTOMER LIST WITH NO DUPLICATE")
cleaned_customers = remove_duplicates(customers)

for customer in cleaned_customers:
    print(customer)
print(f"{ '+' * 50}")

print("SORTED DATA")
print(sort_customers(customers, "name"))
print(f"{ '+' * 50}")
print(sort_customers(customers, "orders"))

print(f"{ '+' * 50}")
print("FILTER BY CITY")
print(filter_customers(customers, "Nairo"))

print(f"{ '+' * 50}")
print(generate_summary(customers))