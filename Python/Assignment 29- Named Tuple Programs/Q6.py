# Assignment 29 
''' Question 6:NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
 '''


from collections import namedtuple

n = int(input("Enter no. of Employees :"))

product = namedtuple("Product",["ProductID","Name","Price"])

prod = []
for i in range(n):
    print("\nEnter Details :")
    id = input("Enter ID of Product :")
    name = input("Enter Name of Product :")
    price = int(input("Enter Price of Product :"))

    P = product(id,name,price)
    prod.append(P)
  
max = 0
min = float('inf')
sum = 0 
print("\nDisplay Details")
for i in prod:
    print(i.ProductID," ",i.Name," ",i.Price)


for i in prod:
    if i.Price>max:
        max = i.Price

    if i.Price < min:
        min = i.Price

for i in prod:
    if i.Price == max:
        print("\nCostliest Product : ")
        print(i.ProductID," ",i.Name," ",i.Price)

    if i.Price == min:
        print("\nCheapest Product: ")
        print(i.ProductID," ",i.Name," ",i.Price)

    sum = sum + i.Price

print("\nAverage : ",sum / n)

print("\nProducts Above ₹50,000: ")
for  i in prod:
    if i.Price>50000:
        print(i.ProductID," ",i.Name," ",i.Price)
