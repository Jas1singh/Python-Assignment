from Assignment6.Customer_Management_System import class_module

customers = []

for i in range(5):
    print(f"\nEnter details of Customer {i + 1}")

    customer_id = int(input("Enter Customer ID: "))
    customer_name = input("Enter Customer Name: ")
    city = input("Enter City: ")
    purchase_amount = float(input("Enter Purchase Amount: "))

    customer = class_module.Customer(
        customer_id,
        customer_name,
        city,
        purchase_amount
    )

    customers.append(customer)


print("\nAll Customers:")
for customer in customers:
    customer.display()

search_city = input("\nEnter City to Search: ")

print(f"\nCustomers from {search_city}:")

for customer in customers:
    if customer.city.lower() == search_city.lower():
        print(
            customer.customer_id,
            customer.customer_name,
            customer.purchase_amount
        )


print("\nCustomers with purchase amount greater than 10000:")

for customer in customers:
    if customer.purchase_amount > 10000:
        print(
            customer.customer_id,
            customer.customer_name,
            customer.purchase_amount
        )


highest_purchase_customer = max(
    customers,
    key=lambda customer: customer.purchase_amount
)

print("\nHighest Purchase Customer:")
print(
    highest_purchase_customer.customer_id,
    highest_purchase_customer.customer_name,
    highest_purchase_customer.purchase_amount
)


total_sales = sum(
    customer.purchase_amount for customer in customers
)

print("\nTotal Sales:")
print(total_sales)


average_purchase = total_sales / len(customers)

print("\nAverage Purchase Amount:")
print(average_purchase)


search_id = int(input("\nSearch Customer Id: "))

found_customer = None

for customer in customers:
    if customer.customer_id == search_id:
        found_customer = customer
        break

if found_customer:
    print("\nCustomer Found:")
    found_customer.display()
else:
    print("\nCustomer Not Found")
